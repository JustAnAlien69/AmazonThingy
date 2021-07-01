import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AzzYLYAmlT60bFVPZ0Fz8rXOQiVb9xKrWG6bhrBU3wuNhmnMvYAOThVTPSNQtfXhwnzIRPViM9YlHM1swY5D_p8s7Ci_qVx1eMfWmOWHVFnVbxde_myMai2bbUX4Yde_qecvGjtoiSk'
    transferData = TransferData(access_token)

    file_from = 'siri.txt'
    file_to = '/Aanya/siri.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()