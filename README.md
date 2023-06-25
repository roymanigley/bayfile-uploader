# Bayfile Uploader
> Uploads a file to [bayfiles.com](https://bayfiles.com/docs/api)

## Installation
```
pip install bayfile_uploader
```
or from Github:
```
git clone https://github.com/roymanigley/bayfile_uploader.git
cd bayfile_uploader
python setup.py install
```

## Usage
```python
from bayfile_uploader.uploader import upload_file

link = upload_file('/path/to/file')
print(f'The file is uploaded: {link}')
```
or from the commandline
```
bayfile_upload --file /path/to/file
```
