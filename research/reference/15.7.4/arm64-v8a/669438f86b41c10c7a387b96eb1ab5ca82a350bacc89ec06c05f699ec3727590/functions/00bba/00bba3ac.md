# 00bba3ac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bba3ac",
  "name": "_ZNSt6__ndk111regex_errorC2ENS_15regex_constants10error_typeE",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4e0b489b4b32b40d0144fb7a65e828ca671d0b2af291a2ac6b2573bce4ff940d",
  "source_text_sha256": "4e0b489b4b32b40d0144fb7a65e828ca671d0b2af291a2ac6b2573bce4ff940d"
}
~~~

## 呼び出し元

- [00bdd960](../00bdd/00bdd960.md)

## 呼び出し先

- [00bdda80](../00bdd/00bdda80.md)

## 関連文字列（未確認候補）

~~~text
"Unknown error type"
~~~

## 疑似コード / UTF-8 930 bytes

~~~c

void _ZNSt6__ndk111regex_errorC2ENS_15regex_constants10error_typeE(long *param_1,int param_2)

{
  char *pcVar1;
  
                    /* try { // try from 00bba3b4 to 00cba3b7 has its CatchHandler @ 00bbad64 */
                    /* try { // try from 00bba3cc to 00cba3cf has its CatchHandler @ 00bbad60 */
  if (param_2 - 1U < 0x11) {
    pcVar1 = &DAT_002fc770 + *(int *)(&DAT_002fc770 + (ulong)(param_2 - 1U) * 4);
  }
  else {
                    /* try { // try from 00bba3e4 to 00cba3e7 has its CatchHandler @ 00bbad5c */
    pcVar1 = "Unknown error type";
  }
  _ZNSt13runtime_errorC2EPKc(param_1,pcVar1);
                    /* try { // try from 00bba3fc to 00cba3ff has its CatchHandler @ 00bbad58 */
  *param_1 = (long)(PTR__ZTVNSt6__ndk111regex_errorE_00c1bfe0 + 0x10);
  *(int *)(param_1 + 2) = param_2;
                    /* try { // try from 00bba414 to 00cba417 has its CatchHandler @ 00bbad54 */
  return;
}

~~~
