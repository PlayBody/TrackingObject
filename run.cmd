for /f "delims=" %%i in ('dir "./moc" /b ^| findstr /i ".ui"') do (
  pyuic6 moc/%%i -o moc/%%~ni.py
)

python app.py