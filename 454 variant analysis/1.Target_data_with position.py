from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIStandalone



f3 = open("Mismatch_total_LOD v3_171103.txt",'r')
f4 = open("Mismatch_total_LOD v3_with position_171116.txt",'w')
f5 = open("Excluded_Mismatch_total_LOD v3_with position_171116.txt",'w')

result_handle = open(r'Blast\out\02.blast_result_total.txt','r')
blast_parser = NCBIStandalone.BlastParser()
blast_iterator = NCBIStandalone.Iterator(result_handle, blast_parser)

      
for line in f3 :
    name = line.split(' ')[0]
    #print name

    for blast_record in blast_iterator:
        if (blast_record.query.split(' ')[0] == name): 
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    mismatch_Number = (hsp.identities[1]-( hsp.identities[0] + hsp.gaps[0] ))
                    Gaps_Number = hsp.gaps[0]
                    Range=range(1,300)
                    insertion=0
                    for a in Range:

                        insertion=0
                        
                        if ( hsp.match[a:a+1] != '|') and (hsp.query[a:a+1] != '-') and (hsp.sbjct[a:a+1] != '-') and ((hsp.query[a:a+1] == 'N') or (hsp.query[a:a+1] == 'A') or (hsp.query[a:a+1] == 'T') or (hsp.query[a:a+1] == 'G') or (hsp.query[a:a+1] == 'C')) and ((hsp.sbjct[a:a+1] == 'N') or(hsp.sbjct[a:a+1] == 'A') or (hsp.sbjct[a:a+1] == 'T') or (hsp.sbjct[a:a+1] == 'G') or (hsp.sbjct[a:a+1] == 'C')) :   
                        #if ( hsp.match[a:a+1] != '|') and (hsp.query[a:a+1] != '-') and (hsp.sbjct[a:a+1] != '-') and (hsp.query[a:a+1] != ' ') and (hsp.sbjct[a:a+1] != ' '):   
                  
                            #f4.write('****Alignment****\n')
                            #f4.write('> '+name+'\n')
                            #f4.write(alignment.length)
                            #print('score:', alignment.score)
                            #print('gaps:', alignment.gaps)
                            #print('e value:', hsp.expect)
                            #print hsp
                            #print (hsp.query[0:1]+'\n')
                            #print a
                            #f4.write(alignment.title+'\t'+str(a+1)+'\t'+hsp.query[a:a+1]+'\t'+hsp.sbjct[a:a+1]+'\t'+name+'\n')

                            for i in range(0,a):
                                if hsp.sbjct[i:i+1] == '-':
                                    insertion+=1
                                else:
                                    insertion+=0

                            #print insertion

                            #CAGGCGCGACTTTT
                            if (hsp.sbjct[0:2] == 'CA'):
                                x = blast_record.query.split()[2].split('=')[1]
                                y = blast_record.query.split()[3].split('=')[1]
                                f4.write(x + '\t' + y + '\t' + alignment.title + '\t' + str(a + 1 - insertion) + '\t' + hsp.query[a:a+1] + '\t' + hsp.sbjct[a:a + 1] + '\t' + name + '\n')
                            
                            elif (hsp.sbjct[0:2] == 'AG'):
                                x = blast_record.query.split()[2].split('=')[1]
                                y = blast_record.query.split()[3].split('=')[1]
                                f4.write(x + '\t' + y + '\t' + alignment.title + '\t' + str(a + 2 - insertion) + '\t' + hsp.query[a:a+1] + '\t' + hsp.sbjct[a:a + 1] + '\t' + name + '\n')
                                #break
                            elif (hsp.sbjct[0:2] == 'GG'):
                                x = blast_record.query.split()[2].split('=')[1]
                                y = blast_record.query.split()[3].split('=')[1]
                                f4.write(x + '\t' + y + '\t' + alignment.title + '\t' + str(a + 3 - insertion) + '\t' + hsp.query[a:a+1] + '\t' + hsp.sbjct[a:a + 1] + '\t' + name + '\n')
                                #break
                            elif (hsp.sbjct[0:4] == 'GCGC'):
                                x = blast_record.query.split()[2].split('=')[1]
                                y = blast_record.query.split()[3].split('=')[1]
                                f4.write(x + '\t' + y + '\t' + alignment.title + '\t' + str(a + 4 - insertion) + '\t' + hsp.query[a:a+1] + '\t' + hsp.sbjct[a:a + 1] + '\t' + name + '\n')

                            elif (hsp.sbjct[0:5] == 'CGCGA'):
                                x = blast_record.query.split()[2].split('=')[1]
                                y = blast_record.query.split()[3].split('=')[1]
                                f4.write(x + '\t' + y + '\t' + alignment.title + '\t' + str(a + 5 - insertion) + '\t' + hsp.query[a:a+1] + '\t' + hsp.sbjct[a:a + 1] + '\t' + name + '\n')

                            elif (hsp.sbjct[0:4] == 'GCGA'):
                                x = blast_record.query.split()[2].split('=')[1]
                                y = blast_record.query.split()[3].split('=')[1]
                                f4.write(x + '\t' + y + '\t' + alignment.title + '\t' + str(a + 6 - insertion) + '\t' + hsp.query[a:a+1] + '\t' + hsp.sbjct[a:a + 1] + '\t' + name + '\n')
                             
                            else :
                                f5.write(name + '\n')
                            #f4.write(hsp.query[0:1]+'\n'+name+'\n')
                            #f4.write(hsp.match[a:a+1]+'\n')
                            #f4.write(hsp.sbjct[a:a+1]+'\n'+'\n')
                            #print hsp.match[a:a+1]
                    

            break

         
            
f3.close()
f4.close()
f5.close()
result_handle.close()

