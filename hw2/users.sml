fun fst(x,y)=x;
fun snd(x,y)=y;

fun getRoles(a,b,c) =
    if b=[] then c
    else if a = fst(hd(b)) then snd(hd(b))::getRoles(a,tl(b),c)
    else getRoles(a,tl(b),c);

fun has(a,b)=
    if a =[] then false
    else if fst(b)=hd(a) then true
    else has(tl(a),b);

fun expandRoles(a,b) = 
    if b = [] then a
    else if has(a,hd(b)) then expandRoles(a@[snd(hd(b))],tl(b))
    else expandRoles(a,tl(b));

fun remove(x,L) = 
    if L=[] then []
    else if x=hd(L) then remove(x,tl(L))
    else hd(L)::remove(x,tl(L));

fun removedupl(L) =
    if L=[] then []
    else hd(L)::removedupl(remove(hd(L),tl(L)));

fun authorizedRoles(a,b,c)=removedupl(expandRoles(getRoles(a,b,[]),c));


fun permissionHelper(a,b,c)=
    if b = [] then c
    else if has(a,hd(b)) then permissionHelper(a,tl(b),c@[snd(hd(b))])
    else permissionHelper(a,tl(b),c);

fun authorizedPermissions(a,b,c)=removedupl(permissionHelper(b,c,[]));
