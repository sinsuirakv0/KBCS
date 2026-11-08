# 00b4cbfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b4cbfc",
  "name": "_ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb",
  "size": 320,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "da3d741c05d436d71234534d6a1d96074f65230343a7e1c30553df8605f7b9de",
  "source_text_sha256": "da3d741c05d436d71234534d6a1d96074f65230343a7e1c30553df8605f7b9de"
}
~~~

## 呼び出し元

- [00bddc40](../00bdd/00bddc40.md)

## 呼び出し先

- [00474b70](../00474/00474b70.md)
- [00551e14](../00551/00551e14.md)
- [00b4cda8](../00b4c/00b4cda8.md)
- [00bdddf0](../00bdd/00bdddf0.md)
- [00bde130](../00bde/00bde130.md)
- [00bde1b0](../00bde/00bde1b0.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 1920 bytes

~~~c

void _ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb(uint param_1)

{
  char cVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
                    /* try { // try from 00b4cc00 to 00c4cc6f has its CatchHandler @ 00b4ddd0 */
  if (DAT_010a1060 == 0) {
                    /* try { // try from 00b4cce8 to 00c4ccf3 has its CatchHandler @ 00b4da7c */
    DAT_010a1100 = 1;
    if ((param_1 & 1) == 0) {
      DAT_010a1100 = 2;
    }
  }
  else {
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv(DAT_010a1060);
    if (DAT_010a1060 == 0) {
      _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
      _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
      if (DAT_010a1060 == 0) {
                    /* try { // try from 00b4cd34 to 00c4cd3f has its CatchHandler @ 00b4da38 */
        FUN_00551e14(uVar2,DAT_010a1098,DAT_010a0fd0,param_1 & 1);
        return;
      }
    }
    uVar3 = _ZNK8firebase3App9GetJNIEnvEv(DAT_010a1060);
    cVar1 = FUN_00474b70(uVar3,DAT_010a1098,DAT_010a0fc8);
    FUN_00551e14(uVar2,DAT_010a1098,DAT_010a0fd0,param_1 & 1);
    if (cVar1 != '\0') {
      return;
    }
                    /* try { // try from 00b4cc90 to 00c4cc9b has its CatchHandler @ 00b4db58 */
    if (DAT_010a1060 == 0) {
      _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
      _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
                    /* try { // try from 00b4ccb4 to 00c4ccbf has its CatchHandler @ 00b4dae8 */
      if (DAT_010a1060 == 0) goto LAB_00b4ccd4;
    }
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
                    /* try { // try from 00b4ccc8 to 00c4cccb has its CatchHandler @ 00b4dac8 */
    cVar1 = FUN_00474b70(uVar2,DAT_010a1098,DAT_010a0fc8);
    if (cVar1 != '\0') {
LAB_00b4ccd4:
      FUN_00b4cda8();
      return;
    }
  }
                    /* try { // try from 00b4cd08 to 00c4cd13 has its CatchHandler @ 00b4da78 */
  return;
}

~~~
