# 00afcffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afcffc.md)

## 関数情報

~~~json
{
  "address": "00afcffc",
  "name": "firebase::Path::Path",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef3c8acbacdc7d515af478197a87af85be81bcfebf013a661e756a445aba873e",
  "source_text_sha256": "ef3c8acbacdc7d515af478197a87af85be81bcfebf013a661e756a445aba873e"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00afd1a0](../00afd/00afd1a0.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bde1c0](../00bde/00bde1c0.md)
- [00bde630](../00bde/00bde630.md)
- [00bdec30](../00bde/00bdec30.md)

## 疑似コード 1/1 / UTF-8 3238 bytes

~~~c

/* firebase::Path::Path(std::__ndk1::vector<std::__ndk1::basic_string<char,
   std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >,
   std::__ndk1::allocator<std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>,
   std::__ndk1::allocator<char> > > > const&) */

void __thiscall firebase::Path::Path(Path *this,vector *param_1)

{
  basic_string *pbVar1;
  basic_string *pbVar2;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> bVar3;
  ulong uVar4;
  long lVar5;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *pbVar6;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *pbVar7;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *pbVar8;
  basic_string *extraout_x1;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *this_00;
  Path local_60 [16];
  void *local_50;
  long local_48;
  
                    /* try { // try from 00afd010 to 00bfd03f has its CatchHandler @ 00af560c */
  lVar5 = tpidr_el0;
  local_48 = *(long *)(lVar5 + 0x28);
  pbVar1 = *(basic_string **)param_1;
  pbVar2 = *(basic_string **)(param_1 + 8);
  uVar4 = (long)pbVar2 - (long)pbVar1;
  if (uVar4 == 0) {
    pbVar8 = (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)0x0;
    this_00 = (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)0x0;
  }
  else {
                    /* try { // try from 00afd040 to 00bfd047 has its CatchHandler @ 00aff388 */
    if (0xaaaaaaaaaaaaaaa < (ulong)(((long)uVar4 >> 3) * -0x5555555555555555)) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    pbVar8 = operator_new(uVar4);
    this_00 = pbVar8;
    for (; pbVar1 != pbVar2; pbVar1 = pbVar1 + 0x18) {
                    /* try { // try from 00afd070 to 00bfd087 has its CatchHandler @ 00aff384 */
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      basic_string(this_00,pbVar1);
      this_00 = this_00 + 0x18;
    }
  }
  FUN_00afd1a0(local_60,pbVar8,this_00);
  NormalizeSlashes(local_60,extraout_x1);
  if (((byte)local_60[0] & 1) != 0) {
    operator_delete(local_50);
  }
                    /* try { // try from 00afd0c0 to 00bfd0d7 has its CatchHandler @ 00aff380 */
  if (pbVar8 != (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
                0x0) {
    if (this_00 != pbVar8) {
      bVar3 = this_00[-0x18];
      pbVar7 = this_00 + -0x18;
      while( true ) {
        pbVar6 = pbVar7;
        if (((byte)bVar3 & 1) != 0) {
          operator_delete(*(void **)(this_00 + -8));
        }
        if (pbVar8 == pbVar6) break;
        bVar3 = pbVar6[-0x18];
        pbVar7 = pbVar6 + -0x18;
        this_00 = pbVar6;
      }
    }
    operator_delete(pbVar8);
  }
  if (*(long *)(lVar5 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* try { // try from 00afd110 to 00bfd11b has its CatchHandler @ 00aff37c */
  return;
}

~~~
