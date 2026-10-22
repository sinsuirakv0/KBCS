# 00bafa3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bafa3c.md)

## 関数情報

~~~json
{
  "address": "00bafa3c",
  "name": "std::__ndk1::__num_put_base::__format_float",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8def53d6a0b5f1e979349cbe210b0986347c2db80867384c362d8a7cd1c49b32",
  "source_text_sha256": "8def53d6a0b5f1e979349cbe210b0986347c2db80867384c362d8a7cd1c49b32"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 2006 bytes

~~~c

/* std::__ndk1::__num_put_base::__format_float(char*, char const*, unsigned int) */

bool std::__ndk1::__num_put_base::__format_float(char *param_1,char *param_2,uint param_3)

{
  uint uVar1;
  bool bVar2;
  char *pcVar3;
  char *pcVar4;
  char cVar5;
  char cVar6;
  
  pcVar3 = param_1;
  if ((param_3 >> 0xb & 1) != 0) {
    pcVar3 = param_1 + 1;
    *param_1 = '+';
  }
  pcVar4 = pcVar3;
  if ((param_3 >> 10 & 1) != 0) {
                    /* try { // try from 00bafa54 to 00cafaab has its CatchHandler @ 00bafa54
                       catch() { ... } // from try @ 00bafa54 with catch @ 00bafa54
                       catch() { ... } // from try @ 00bafeec with catch @ 00bafa54
                       catch() { ... } // from try @ 00bb01a0 with catch @ 00bafa54
                       catch() { ... } // from try @ 00bb051c with catch @ 00bafa54
                       catch() { ... } // from try @ 00bb0924 with catch @ 00bafa54
                       catch() { ... } // from try @ 00bb0cdc with catch @ 00bafa54 */
    pcVar4 = pcVar3 + 1;
    *pcVar3 = '#';
  }
  uVar1 = param_3 & 0x104;
  pcVar3 = pcVar4;
  if (uVar1 != 0x104) {
    pcVar3 = pcVar4 + 2;
    pcVar4[0] = '.';
    pcVar4[1] = '*';
  }
  cVar6 = *param_2;
  while (cVar6 != '\0') {
    param_2 = param_2 + 1;
    *pcVar3 = cVar6;
    pcVar3 = pcVar3 + 1;
    cVar6 = *param_2;
  }
  if (uVar1 == 0x100) {
                    /* try { // try from 00bafaac to 00cafb0b has its CatchHandler @ 00bb0d0c */
    bVar2 = (param_3 & 0x4000) == 0;
    cVar5 = 'E';
    cVar6 = 'e';
  }
  else if (uVar1 == 4) {
    bVar2 = (param_3 & 0x4000) == 0;
    cVar5 = 'F';
    cVar6 = 'f';
  }
  else if (uVar1 == 0x104) {
    bVar2 = (param_3 & 0x4000) == 0;
    cVar5 = 'A';
    cVar6 = 'a';
  }
  else {
    bVar2 = (param_3 & 0x4000) == 0;
    cVar5 = 'G';
    cVar6 = 'g';
  }
  if (!bVar2) {
    cVar6 = cVar5;
  }
  *pcVar3 = cVar6;
  return uVar1 != 0x104;
}

~~~
