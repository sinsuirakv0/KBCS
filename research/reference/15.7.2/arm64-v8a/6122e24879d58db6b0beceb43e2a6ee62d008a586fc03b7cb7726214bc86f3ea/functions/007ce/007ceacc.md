# 007ceacc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007ceacc.md)

## 関数情報

~~~json
{
  "address": "007ceacc",
  "name": "FUN_007ceacc",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d2e24616de8e236149a3987da9b448e3129a0108818a7e93504aba8ac7c75bc",
  "source_text_sha256": "5d2e24616de8e236149a3987da9b448e3129a0108818a7e93504aba8ac7c75bc"
}
~~~
## 呼び出し元

- [0073fa38](../0073f/0073fa38.md)
- [00749514](../00749/00749514.md)
- [0075bc70](../0075b/0075bc70.md)
- [007e9118](../007e9/007e9118.md)
- [007ef4ec](../007ef/007ef4ec.md)
- [0083f65c](../0083f/0083f65c.md)
- [0086b704](../0086b/0086b704.md)
- [00a52458](../00a52/00a52458.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [00bdaf40](../00bda/00bdaf40.md)

## 疑似コード 1/1 / UTF-8 1630 bytes

~~~c

undefined4 FUN_007ceacc(long param_1,int param_2)

{
  undefined8 *puVar1;
  long *plVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  
  puVar1 = *(undefined8 **)(param_1 + 0x20);
  puVar3 = puVar1;
  if (puVar1 == (undefined8 *)0x0) {
    return 0;
  }
  do {
    if (*(int *)((long)puVar3 + 0x1c) <= param_2) {
      if (param_2 <= *(int *)((long)puVar3 + 0x1c)) break;
      puVar3 = puVar3 + 1;
    }
    puVar3 = (undefined8 *)*puVar3;
    if (puVar3 == (undefined8 *)0x0) {
      return 0;
    }
  } while( true );
LAB_007ceb18:
  puVar3 = puVar1;
  if (*(int *)((long)puVar3 + 0x1c) <= param_2) {
    if (param_2 <= *(int *)((long)puVar3 + 0x1c)) goto LAB_007cebb0;
    puVar1 = (undefined8 *)puVar3[1];
    if ((undefined8 *)puVar3[1] == (undefined8 *)0x0) {
      puVar4 = puVar3 + 1;
      goto LAB_007ceb60;
    }
    goto LAB_007ceb18;
  }
  puVar1 = (undefined8 *)*puVar3;
  puVar4 = puVar3;
  if ((undefined8 *)*puVar3 == (undefined8 *)0x0) {
LAB_007ceb60:
    puVar1 = operator_new(0x28);
    *puVar1 = 0;
    puVar1[1] = 0;
    puVar1[2] = puVar3;
    *puVar4 = puVar1;
    plVar2 = *(long **)(param_1 + 0x18);
    *(int *)((long)puVar1 + 0x1c) = param_2;
    *(undefined4 *)(puVar1 + 4) = 0;
    puVar3 = puVar1;
    if (*plVar2 != 0) {
      *(long *)(param_1 + 0x18) = *plVar2;
      puVar3 = (undefined8 *)*puVar4;
    }
    FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar3);
    *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
    puVar3 = puVar1;
LAB_007cebb0:
    return *(undefined4 *)(puVar3 + 4);
  }
  goto LAB_007ceb18;
}

~~~
