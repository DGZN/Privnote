### Setup

```
pip install pyinstaller pyperclip pyPrivnote
```

#### Find python

>UNIX/LINUX/OSX 

```
which python
```

>WINDOWS

```
where python
```

Edit ```hook-pkg_resources.py``` in ```{path_to_python}``` ```/site-packages/PyInstaller/hooks/)```

Add

```hiddenimports.append('pkg_resources.py2_warn')```

between these two lines of code:

```hiddenimports = collect_submodules('pkg_resources._vendor')```

and

```excludedimports = ['__main__']```

See: https://stackoverflow.com/questions/59035724/python-error-no-module-named-pkg-resources

### Build Privnote


```
pyinstaller -F privnote.py
```