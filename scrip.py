# Print array of subsequent character ordinal offsets in string s
s = r'''    print!("fn main() {{\n    let p:&[i8] = &{:?};\n", p);
    let mut c = 0;
    for x in p.iter() {
        c += *x;
        print!("{}", (c as u8) as char);
    }
}
'''
arr = [ord(s[0])]
for p,n in zip(s, s[1:]):
    arr.append(ord(n) - ord(p))
print(arr)
print(len(arr))
