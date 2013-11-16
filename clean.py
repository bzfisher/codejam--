import sys, datetime, numpy
dataset = sys.argv[1]
clean_dataset = sys.argv[2]

class Clean:

  def strip(self, filename):
    output = 'clean_' + filename
    with open(filename, 'r') as dataset:
      with open(output, 'w') as clean_dataset:
        for row in dataset:
          row_list = row.split(',')
          if row_list[1] == '':
            pass
          else:
            # extract stuff
            date_string = row_list.pop(0)
            energy = row_list.pop(4)
            
            # hack stuff
            date_object = datetime.datetime.strptime(date_string[:-6], '%Y-%m-%dT%H:%M')
            row_list.append(str(date_object.isoweekday()))
            row_list.append(str(date_object.month))
            
            # working hours
            if (date_object.hour >= 9) and (date_object.hour <= 17):
              row_list.append(str(1))
            else:
              row_list.append(str(0))
              
            # school session
            if (date_object.year == 2011):
              if (date_object.month == 9) and (date_object.day == 5):
                row_list.append(str(0)) # labor day
              elif (date_object.month == 10) and (date_object.day == 10):
                row_list.append(str(0)) # thanksgiving
              elif (date_object.month < 9):
                row_list.append(str(0))
              elif (date_object.month == 12) and (date_object.day > 22):
                row_list.append(str(0))
              else:
                row_list.append(str(1))
                   
            elif (date_object.year == 2012):
              if (date_object.month == 9) and (date_object.day == 3):
                row_list.append(str(0)) # labor day
              elif (date_object.month == 10) and (date_object.day == 8):
                row_list.append(str(0)) # thanksgivng
              elif (date_object.month == 4) and (date_object.day == 6):
                row_list.append(str(0)) # good friday
              elif (date_object.month == 4) and (date_object.day == 9):
                row_list.append(str(0)) # easter
              elif (date_object.month == 1) and (date_object.day < 3):
                row_list.append(str(0))
              elif (date_object.month > 4) and (date_object.month < 9) :
                row_list.append(str(0))
              elif (date_object.month == 12) and (date_object.day > 19):
                row_list.append(str(0))
              else:
                row_list.append(str(1))
                
            elif (date_object.year == 2013):
              if (date_object.month == 9) and (date_object.day == 2):
                row_list.append(str(0)) # labor day
              elif (date_object.month == 10) and (date_object.day == 14):
                row_list.append(str(0)) # thanksgivng
              elif (date_object.month == 3) and (date_object.day == 29):
                row_list.append(str(0)) # good friday
              elif (date_object.month == 4) and (date_object.day == 1):
                row_list.append(str(0)) # easter
              elif (date_object.month == 1) and (date_object.day < 3):
                row_list.append(str(0))
              elif (date_object.month > 4) and (date_object.month < 9) :
                row_list.append(str(0))
              elif (date_object.month == 12) and (date_object.day > 19):
                row_list.append(str(0))
              else:
                row_list.append(str(1))
                     
            # finalize stuff
            row_list.append(energy)
            clean_dataset.write(','.join(row_list))
          
  def load(self, dataset):
    data = numpy.genfromtxt(dataset, delimiter=',')
  
if __name__ == '__main__':
  root = Clean()
  root.strip(dataset)
  root.load(clean_dataset)
