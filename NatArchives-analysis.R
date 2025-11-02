library(tidyverse)

path <- readline("enter path:") %>% 
  str_replace_all('"',"") %>% 
  str_replace_all("\\\\","/")


data <- read.csv(path)

data$month <- data$timestamp %>% ymd_hms() %>% floor_date(unit = "month")

mime_counts <- data %>% group_by(urltail,month,mime) %>% count(mime)

library(ggplot2)

ggplot(mime_counts, aes(x = month, y = n, col = mime))+
      geom_line(linewidth = 0.8)+
  labs(title = "count of mime per month")

ggplot(mime_counts, aes(x = month, y = n, col = mime))+
  geom_line(linewidth = 0.8)+
  facet_grid(rows = vars(urltail),scales = "free")+
  labs(title = "monthly mime counts by url www.nhs.uk/conditions/...")

ggplot(mime_counts, aes(x = month, y = n)) +
  geom_area(aes(fill = mime), position = "stack")+
  labs(title = "number of archives, grouped by mime")
  

#ggplot(mime_counts, aes(x = month,y=n)) +
#  geom_area(aes(fill = urltail), position = "stack")+
#  labs(title = "number of archives, grouped by url")


data %>% filter(status == 200, mime == "text/html", length> 1000) %>% 
  ggplot(aes(x = ymd_hms(timestamp), y=length, col = urltail))+
         geom_line(linewidth = 0.8)+
  labs(title = "data size (length) across time")

