

def split(filename):
    from PyPDF2 import PdfFileReader, PdfFileWriter
    
    inputFile = PdfFileReader(open('temp_uploads/'+filename, "rb")) #read binary
    
    for pageNumber in xrange(inputFile.numPages):
        output = PdfFileWriter()
        
        output.addPage(inputFile.getPage(pageNumber))
        
        newFile = "".join(['temp_results/',filename.split('.pdf')[0], str(pageNumber), ".pdf"])
        
        with open(newFile, 'wb') as outputStream:
            output.write(outputStream)
    
    return "done"
        
        
    
    