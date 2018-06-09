def resetSource(filename):
    import shutil
    import os
    
    # delete source file
    filePath = 'temp_uploads/{}'.format(filename)
    os.remove(filePath)
    
    # empty source folder
    shutil.rmtree('temp_results') 
    os.mkdir('temp_results')
    
    return 
    
def deleteZip():
    import os
    import shutil
    
    print "running deleteZip"
    if os.path.exists('zipped_results/results.zip'):
        print "removing zip file"
        shutil.rmtree('zipped_results') 

    return 
    
    