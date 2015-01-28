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

## Reason for current design
Initially, we considered using a parser, but realized that bracket/environment matching was mostly unnecessary for our use case. Next, as we started to implement a state-machine, we realized that even that was unnecessary, because most things could be accomplished by straight substitution. Even the stateful aspects of the program had no real effect on transitions.

Thusly, a script that's mostly just string substitutions with a little state added on for block environments was implemented.
