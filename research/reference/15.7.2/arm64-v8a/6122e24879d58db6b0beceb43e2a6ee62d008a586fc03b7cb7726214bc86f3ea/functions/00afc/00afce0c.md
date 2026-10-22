# 00afce0c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afce0c.md)

## 関数情報

~~~json
{
  "address": "00afce0c",
  "name": "firebase::Path::NormalizeSlashes",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee3cf131b8e401fb658494d3a5dbfb9c429c1569d6cfe81133cd87d0aab9ea90",
  "source_text_sha256": "ee3cf131b8e401fb658494d3a5dbfb9c429c1569d6cfe81133cd87d0aab9ea90"
}
~~~
## 呼び出し元

- [00bdec30](../00bde/00bdec30.md)

## 呼び出し先

- [00bdb030](../00bdb/00bdb030.md)
- [00bdec50](../00bde/00bdec50.md)
- [00bdec70](../00bde/00bdec70.md)

## 疑似コード 1/1 / UTF-8 3634 bytes

~~~c

/* firebase::Path::NormalizeSlashes(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>,
   std::__ndk1::allocator<char> > const&) */

void __thiscall firebase::Path::NormalizeSlashes(Path *this,basic_string *param_1)

{
  Path *pPVar1;
  ulong uVar2;
  Path PVar3;
  Path *pPVar4;
  bool bVar5;
  long lVar6;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *in_x8;
  Path *pPVar7;
  ulong uVar8;
  Path *pPVar9;
  Path *pPVar10;
  bool bVar11;
  
  *(undefined8 *)in_x8 = 0;
  *(undefined8 *)(in_x8 + 8) = 0;
  *(undefined8 *)(in_x8 + 0x10) = 0;
  PVar3 = *this;
  uVar8 = *(ulong *)(this + 8);
  pPVar9 = *(Path **)(this + 0x10);
  bVar5 = ((byte)PVar3 & 1) == 0;
  pPVar10 = pPVar9;
  uVar2 = uVar8;
  if (bVar5) {
    pPVar10 = this + 1;
    uVar2 = (ulong)((byte)PVar3 >> 1);
  }
  if (uVar2 != 0) {
    pPVar1 = this + 1;
    bVar11 = true;
    do {
      uVar2 = (ulong)((byte)PVar3 >> 1);
      pPVar4 = pPVar1;
                    /* try { // try from 00afceac to 00bfcec3 has its CatchHandler @ 00aff3ac */
      if (!bVar5) {
        uVar2 = uVar8;
        pPVar4 = pPVar9;
      }
      pPVar9 = pPVar10;
                    /* try { // try from 00afcec4 to 00bfcf27 has its CatchHandler @ 00af560c */
      if ((pPVar4 + uVar2 != pPVar10) &&
         (lVar6 = __strchr_chk(&DAT_0029583d,*pPVar10,2), lVar6 != 0)) {
        do {
          pPVar9 = pPVar4 + uVar2;
          if (pPVar4 + (uVar2 - 1) == pPVar10) break;
          pPVar9 = pPVar10 + 1;
          lVar6 = __strchr_chk(&DAT_0029583d,pPVar10[1],2);
          pPVar10 = pPVar9;
        } while (lVar6 != 0);
      }
      uVar8 = (ulong)((byte)*this >> 1);
      pPVar4 = pPVar1;
      if (((byte)*this & 1) != 0) {
        uVar8 = *(ulong *)(this + 8);
        pPVar4 = *(Path **)(this + 0x10);
      }
                    /* try { // try from 00afcf28 to 00bfcf2f has its CatchHandler @ 00aff3a8 */
      pPVar10 = pPVar9;
      if ((pPVar4 + uVar8 != pPVar9) && (lVar6 = __strchr_chk(&DAT_0029583d,*pPVar9,2), lVar6 == 0))
      {
        pPVar7 = pPVar9;
        do {
          pPVar10 = pPVar4 + uVar8;
          if (pPVar4 + (uVar8 - 1) == pPVar7) break;
                    /* try { // try from 00afcf58 to 00bfcf6f has its CatchHandler @ 00aff3a4 */
          pPVar10 = pPVar7 + 1;
          pPVar7 = pPVar7 + 1;
          lVar6 = __strchr_chk(&DAT_0029583d,*pPVar10,2);
          pPVar10 = pPVar7;
        } while (lVar6 == 0);
        if (pPVar10 != pPVar9) {
          if (!bVar11) {
                    /* try { // try from 00afcf80 to 00bfcf87 has its CatchHandler @ 00aff3a0 */
            std::__ndk1::
            basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::append
                      (in_x8,"/",1);
          }
                    /* try { // try from 00afcfb0 to 00bfcfc7 has its CatchHandler @ 00aff39c */
          std::__ndk1::
          basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
          insert<std::__ndk1::__wrap_iter<char_const*>>();
          bVar11 = false;
        }
      }
      PVar3 = *this;
      uVar8 = *(ulong *)(this + 8);
      pPVar9 = *(Path **)(this + 0x10);
      bVar5 = ((byte)PVar3 & 1) == 0;
      uVar2 = (ulong)((byte)PVar3 >> 1);
      pPVar4 = pPVar1;
      if (!bVar5) {
        uVar2 = uVar8;
        pPVar4 = pPVar9;
      }
    } while (pPVar4 + uVar2 != pPVar10);
  }
                    /* try { // try from 00afcff8 to 00bfd00f has its CatchHandler @ 00aff38c */
  return;
}

~~~
