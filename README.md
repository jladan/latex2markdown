# latex2markdown
A very quick and limited latex -> markdown converter.

Not something to be proud of.

## Limitations
The only supported environments are:
- itemize
- enumerate
- quote
- verbatim

The `\begin` and `\end` macros for these environments must be on their own line, because anything following or preceding them will be obliterated. Nested environments are also basically unsupported (even for lists).

Supported span elements are:
- `\emph` -> emphasis
- `\textbf` -> bold font
- `\verb;;` -> code
- `\includegraphics` -> image

At the moment, `\verb` must use a semicolon (`;`) as the delimiter, and `\includegraphics` cannot handle optional arguments. Nested span elements are **definitely** not supported.

## Future additions
- Support for different delimeters in `\verb` statements
- support for optional argument (at least stripping them) for `\includegraphics`
- support for nested lists
