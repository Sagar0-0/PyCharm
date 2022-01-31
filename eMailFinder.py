import re


def extractEmails(str):
    return re.findall("[a-zA-Z0-9\.\_\-]+[@][a-z]+[.][a-z]{2,}", str)


if __name__ == '__main__':
    s = "sagar.0dev@gmail.cwromwt sedfy1@adfe.ertw rrt  sryh sry sagar@gmail.in wrtje erthyerhfrha  sszr wef@srd.com aeryaerry22222w4634@ ssnjlf@sdrf.ij"
    lis = extractEmails(s)
    for i in lis:
        print(i)
