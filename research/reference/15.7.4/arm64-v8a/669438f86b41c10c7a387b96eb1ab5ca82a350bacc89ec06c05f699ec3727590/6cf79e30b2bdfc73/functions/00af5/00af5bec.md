# 00af5bec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00af5bec.md)

## 関数情報

~~~json
{
  "address": "00af5bec",
  "name": "_ZN8firebase4util20JniByteArrayToVectorEP7_JNIEnvP8_jobject",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a3dd07f7e3b42345148b85c96aaf5a2ef0a9a42da94f25e5a6a3d29d2b0792d8",
  "source_text_sha256": "a3dd07f7e3b42345148b85c96aaf5a2ef0a9a42da94f25e5a6a3d29d2b0792d8"
}
~~~
## 呼び出し元

- [00bde5f0](../00bde/00bde5f0.md)

## 呼び出し先

- [00bde7e0](../00bde/00bde7e0.md)

## 疑似コード 1/1 / UTF-8 1717 bytes

~~~c

void _ZN8firebase4util20JniByteArrayToVectorEP7_JNIEnvP8_jobject
               (undefined8 *param_1,long *param_2,undefined8 param_3)

{
  int iVar1;
  
                    /* try { // try from 00af5bf4 to 00bf5bfb has its CatchHandler @ 00affcd0 */
  *param_1 = 0;
  param_1[1] = 0;
                    /* try { // try from 00af5c00 to 00bf5c07 has its CatchHandler @ 00affcb8 */
  param_1[2] = 0;
                    /* try { // try from 00af5c0c to 00bf5c13 has its CatchHandler @ 00affcac */
                    /* try { // try from 00af5c18 to 00bf5c1f has its CatchHandler @ 00affc94 */
  iVar1 = (**(code **)(*param_2 + 0x558))();
  if (iVar1 != 0) {
                    /* try { // try from 00af5c24 to 00bf5c2b has its CatchHandler @ 00affc88 */
    _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE8__appendEm(param_1,(long)iVar1);
                    /* try { // try from 00af5c30 to 00bf5c37 has its CatchHandler @ 00affc70 */
                    /* try { // try from 00af5c3c to 00bf5c43 has its CatchHandler @ 00affc64 */
                    /* try { // try from 00af5c48 to 00bf5c4f has its CatchHandler @ 00affc4c */
    (**(code **)(*param_2 + 0x640))(param_2,param_3,0,iVar1,*param_1);
  }
                    /* try { // try from 00af5c54 to 00bf5c5b has its CatchHandler @ 00affc40 */
                    /* try { // try from 00af5c60 to 00bf5c67 has its CatchHandler @ 00affc28 */
                    /* WARNING: Could not recover jumptable at 0x00af5c6c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
                    /* try { // try from 00af5c6c to 00bf5c73 has its CatchHandler @ 00affc1c */
  (**(code **)(*param_2 + 0xb8))(param_2,param_3);
  return;
}

~~~
