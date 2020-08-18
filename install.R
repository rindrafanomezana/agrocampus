local({r <- getOption("repos")
       r["CRAN"] <- "http://cran.r-project.org" 
       options(repos=r)
})
install.packages('IRkernel') 
IRkernel::installspec()
install.packages("ranger")
