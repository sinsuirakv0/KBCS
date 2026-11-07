# 00bafaa4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00baf998`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf998.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bafaa4",
  "name": "_ZNSt6__ndk114__num_put_base12__format_intEPcPKcbj",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e79090be92b493f74963e7274026d58b7edd228d118b564784e80c94d0cb61e5",
  "source_text_sha256": "e79090be92b493f74963e7274026d58b7edd228d118b564784e80c94d0cb61e5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1877 bytes

~~~c

void _ZNSt6__ndk114__num_put_base12__format_intEPcPKcbj
               (char *param_1,char *param_2,uint param_3,uint param_4)

{
  char *pcVar1;
  char *pcVar2;
  char cVar3;
  
  pcVar1 = param_1;
  if (((((param_4 >> 0xb & 1) != 0) && ((param_4 & 0x4a) != 8)) && ((param_4 & 0x4a) != 0x40)) &&
     ((param_3 & 1) != 0)) {
                    /* try { // try from 00bafac8 to 00cafacf has its CatchHandler @ 00bafb40 */
    pcVar1 = param_1 + 1;
    *param_1 = '+';
  }
  pcVar2 = pcVar1;
  if ((param_4 >> 9 & 1) != 0) {
    pcVar2 = pcVar1 + 1;
    *pcVar1 = '#';
  }
  cVar3 = *param_2;
  while (cVar3 != '\0') {
    param_2 = param_2 + 1;
    *pcVar2 = cVar3;
    pcVar2 = pcVar2 + 1;
    cVar3 = *param_2;
  }
                    /* try { // try from 00bafaf8 to 00cafaff has its CatchHandler @ 00bafb3c */
                    /* try { // try from 00bafb00 to 00cafb2b has its CatchHandler @ 00baf9fc */
  if ((param_4 & 0x4a) != 0x40) {
    if ((param_4 & 0x4a) == 8) {
      cVar3 = 'x';
      if ((param_4 & 0x4000) != 0) {
        cVar3 = 'X';
      }
      *pcVar2 = cVar3;
      return;
    }
    cVar3 = 'd';
                    /* try { // try from 00bafb34 to 00cafb3b has its CatchHandler @ 00bafb3c */
                    /* catch() { ... } // from try @ 00bafaf8 with catch @ 00bafb3c
                       catch() { ... } // from try @ 00bafb34 with catch @ 00bafb3c
                       try { // try from 00bafb3c to 00cafb5f has its CatchHandler @ 00baf9fc */
    if ((param_3 & 1) == 0) {
      cVar3 = 'u';
    }
                    /* catch() { ... } // from try @ 00bafac8 with catch @ 00bafb40
                       catch() { ... } // from try @ 00bafb2c with catch @ 00bafb40 */
    *pcVar2 = cVar3;
    return;
  }
  *pcVar2 = 'o';
                    /* try { // try from 00bafb2c to 00cafb33 has its CatchHandler @ 00bafb40 */
  return;
}

~~~
