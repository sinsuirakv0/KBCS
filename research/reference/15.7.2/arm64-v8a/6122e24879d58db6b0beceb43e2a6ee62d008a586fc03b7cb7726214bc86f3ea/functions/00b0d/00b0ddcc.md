# 00b0ddcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b0ddcc.md)

## 関数情報

~~~json
{
  "address": "00b0ddcc",
  "name": "_JNIEnv::CallStaticBooleanMethod",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "443bdb9370567ca1bdedd78a3d8a18c4600bb6c05e1068a3cdd36311726da969",
  "source_text_sha256": "443bdb9370567ca1bdedd78a3d8a18c4600bb6c05e1068a3cdd36311726da969"
}
~~~
## 呼び出し元

- [00bdef90](../00bde/00bdef90.md)

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 1155 bytes

~~~c

/* _JNIEnv::CallStaticBooleanMethod(_jclass*, _jmethodID*, ...) */

void _JNIEnv::CallStaticBooleanMethod(_jclass *param_1,_jmethodID *param_2,...)

{
  long lVar1;
  undefined8 in_x3;
  undefined8 in_x4;
  undefined8 in_x5;
  undefined8 in_x6;
  undefined8 in_x7;
  long lVar2;
  undefined1 auStack_a0 [8];
  undefined8 local_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined1 *local_70;
  undefined1 **ppuStack_68;
  undefined1 *puStack_60;
  undefined8 uStack_58;
  
  lVar1 = tpidr_el0;
  lVar2 = *(long *)(lVar1 + 0x28);
  puStack_60 = auStack_a0;
  ppuStack_68 = &local_70;
  uStack_58 = 0xffffff80ffffffd8;
  local_98 = in_x3;
  uStack_90 = in_x4;
  local_88 = in_x5;
  uStack_80 = in_x6;
  local_78 = in_x7;
  local_70 = (undefined1 *)register0x00000008;
  (**(code **)(*(long *)param_1 + 0x3b0))();
  if (*(long *)(lVar1 + 0x28) == lVar2) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00b0de64 to 00c0de6b has its CatchHandler @ 00b0dfec */
  __stack_chk_fail();
}

~~~
