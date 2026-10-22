# 00bace3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bace3c.md)

## 関数情報

~~~json
{
  "address": "00bace3c",
  "name": "std::__ndk1::codecvt<char32_t,char8_t,mbstate_t>::do_out",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a1031e17e53e42d5b4ef0c9e17bac75f955349754399bface9537a4ea76b83f4",
  "source_text_sha256": "a1031e17e53e42d5b4ef0c9e17bac75f955349754399bface9537a4ea76b83f4"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 2365 bytes

~~~c

/* std::__ndk1::codecvt<char32_t, char8_t, mbstate_t>::do_out(mbstate_t&, char32_t const*, char32_t
   const*, char32_t const*&, char8_t*, char8_t*, char8_t*&) const */

undefined8 __thiscall
std::__ndk1::codecvt<char32_t,char8_t,mbstate_t>::do_out
          (codecvt<char32_t,char8_t,mbstate_t> *this,mbstate_t *param_1,wchar32 *param_2,
          wchar32 *param_3,wchar32 **param_4,uchar *param_5,uchar *param_6,uchar **param_7)

{
  wchar32 wVar1;
  byte bVar2;
  undefined8 uVar3;
  byte *pbVar4;
  
  do {
    if (param_3 <= param_2) {
      uVar3 = 0;
                    /* catch() { ... } // from try @ 00bacd90 with catch @ 00bacf48 */
LAB_00bacf58:
                    /* catch() { ... } // from try @ 00bace28 with catch @ 00bacf58 */
      *param_4 = param_2;
      *param_7 = param_5;
      return uVar3;
    }
    wVar1 = *param_2;
    if (0x10 < (uint)wVar1 >> 0x10 || (wVar1 & 0xfffff800U) == 0xd800) {
      uVar3 = 2;
      goto LAB_00bacf58;
    }
                    /* try { // try from 00bace78 to 00cad07b has its CatchHandler @ 00bacc84 */
    bVar2 = (byte)wVar1;
    if ((uint)wVar1 < 0x80) {
      if ((long)param_6 - (long)param_5 < 1) goto LAB_00bacf54;
      pbVar4 = param_5 + 1;
      *param_5 = bVar2;
    }
    else if ((uint)wVar1 < 0x800) {
      if ((long)param_6 - (long)param_5 < 2) goto LAB_00bacf54;
      pbVar4 = param_5 + 2;
      *param_5 = (byte)((uint)wVar1 >> 6) | 0xc0;
      param_5[1] = bVar2 & 0x3f | 0x80;
    }
    else if ((uint)wVar1 >> 0x10 == 0) {
      if ((long)param_6 - (long)param_5 < 3) {
LAB_00bacf54:
        uVar3 = 1;
        goto LAB_00bacf58;
      }
      pbVar4 = param_5 + 3;
      *param_5 = (byte)((uint)wVar1 >> 0xc) | 0xe0;
      param_5[1] = (byte)((uint)wVar1 >> 6) & 0x3f | 0x80;
      param_5[2] = bVar2 & 0x3f | 0x80;
    }
    else {
      if ((long)param_6 - (long)param_5 < 4) goto LAB_00bacf54;
      pbVar4 = param_5 + 4;
      *param_5 = (byte)((uint)wVar1 >> 0x12) | 0xf0;
      param_5[1] = (byte)((uint)wVar1 >> 0xc) & 0x3f | 0x80;
      param_5[2] = (byte)((uint)wVar1 >> 6) & 0x3f | 0x80;
      param_5[3] = bVar2 & 0x3f | 0x80;
    }
                    /* try { // try from 00bace54 to 00cace77 has its CatchHandler @ 00bacff8 */
    param_2 = param_2 + 1;
    param_5 = pbVar4;
  } while( true );
}

~~~
