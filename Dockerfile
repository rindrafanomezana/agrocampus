FROM pnavaro/jupyter
RUN pip install nbcourse
ENTRYPOINT ["nbcourse"]
