# C formatter for 42 norminette

This is C language formatter that fits 42 norminette.
I know you are already a good Human norm.
It's just for convenience.

## How to use

1. Install clang-format.
- MacOS
```
$ brew install clang-format
```

2. Copy `.clang-format` in your Workspace directory.

3. VSCode Settings
- Set Default Formatter as clang-format.
- Turn off `Format On Paste`, `Format On Save`.
- Or You can just copy this in your `.vscode/settings.json` file.
```
"editor.defaultFormatter": "xaver.clang-format",
"editor.formatOnPaste": false,
"editor.formatOnSave": false,
```

4. Execute code formatting
- On Windows: Shift + Alt + F
- On Mac: Shift + Option + F
- On Linux: Ctrl + Shift + I

## Caution

It's not perfect.
**You should format these rules MANUALLY after auto-formatting.**
- `global aligned`
- `declarations aligned`
- `declarations must be followed by one empty line`
- `Empty line`
```
int         aaaa = 12;
float       b = 23;
std::string ccc = 23;
```


Recommended to set in `Workspace Preference`

Feel free to report issues or contribute. :)

## TODO

- [ ] local variable hoisting  

```
puts("hello");
int a = 1;
printf("%d\n", a);
```
to:
```
int a;

puts("hello");
a = 1;
printf("%d\n", a);
```

- [ ] Remove empty lines after local variable declaration  

```
int a;
int b;

printf("%d\n", a);

printf("%d\n", b);
```
to:
```
int a;
int b;

printf("%d\n", a);
printf("%d\n", b);
```

- [ ] Header file and global variable alignement

- [ ] Preprocessor directive indentation  
```
#          ifdef A
#define BUF 45
#                    endif
```
to:
```
#ifdef A
# define BUF 45
#endif
```

- [ ] A VSCode extension
- [ ] A vim  plugin
- [ ] Atom/sublime text/emacs?
