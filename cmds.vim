set autoread | au CursorHold * checktime | call feedkeys("lh")

"au VimLeave * !./clean.sh %:p
