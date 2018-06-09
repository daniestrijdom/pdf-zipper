
def makeZip():
    import shutil
    import os
    
    os.mkdir('zipped_results')
    
    return shutil.make_archive('zipped_results/results', 'zip', 'temp_results')
        
    
        