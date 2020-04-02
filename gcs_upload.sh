#!/bin/shell

STRAGE_NAME=$1
gsutil cp -r public/* gs://${STRAGE_NAME}
gsutil acl ch -r -u AllUsers:R gs://${STRAGE_NAME}
