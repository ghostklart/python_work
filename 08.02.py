def favorite_book(title):
    rmsg = f"Your favorite book is: {title.title()}."
    print(rmsg)
qmsg = "What is your favorite book? "
title = input(qmsg)
favorite_book(title)