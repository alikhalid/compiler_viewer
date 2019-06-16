set autoread
au CursorHold,CursorHoldI * checktime
call feedkeys("lh")
set noswapfile
set syntax=logtalk
set updatetime=500

map <F1> /error:<cr> <bar> ggn<esc>
map <F5> :edit!<cr> <bar> :so scripts/cmds.vim<cr>
