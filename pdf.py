

def split(filename):
    from PyPDF2 import PdfFileReader, PdfFileWriter
    import os
    
    # create temp directory if it doesn't exist
    if not os.path.exists('temp_results'):
        os.mkdir('temp_results')
    
    # read file
    inputFile = PdfFileReader(open('temp_uploads/'+filename, "rb")) #read binary
    
    # split files
    for pageNumber in xrange(inputFile.numPages):
        output = PdfFileWriter()
        
        output.addPage(inputFile.getPage(pageNumber))
        
        newFile = "".join(['temp_results/',filename.split('.pdf')[0], str(pageNumber), ".pdf"])
        
        with open(newFile, 'wb') as outputStream:
            output.write(outputStream)
    
    
    return "done"
        
        
    
    