# 00c3dfcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00c3dfcc",
  "name": "FUN_00c3dfcc",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d09e18a45cafc59f2c94541184fbf7ec026038d64ba3038730ce753708a8e2b6",
  "source_text_sha256": "d09e18a45cafc59f2c94541184fbf7ec026038d64ba3038730ce753708a8e2b6"
}
~~~

## 呼び出し元

- [00c3b208](../00c3b/00c3b208.md)

## 呼び出し先

- [00c590c0](../00c59/00c590c0.md)
- [00c5b0c0](../00c5b/00c5b0c0.md)

## 疑似コード / UTF-8 1686 bytes

~~~c

void FUN_00c3dfcc(long param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                 undefined8 *param_5,undefined8 *param_6,undefined4 *param_7,undefined1 *param_8)

{
  undefined4 uVar1;
  undefined1 uVar2;
  undefined8 *puVar3;
  long lVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  void *pvVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  
  pvVar8 = *(void **)(param_1 + 0x1330);
  lVar4 = *(long *)((long)pvVar8 + 8);
  puVar3 = pvVar8;
  if (lVar4 - 4000U < 0xfffffffffffff010) {
    puVar3 = malloc(0x1000);
    if (puVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar4 = 0;
    *puVar3 = pvVar8;
    puVar3[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar3;
  }
  *(long *)((long)puVar3 + 8) = lVar4 + 0x50;
  *(undefined ***)((long)puVar3 + lVar4 + 0x10) = &PTR_FUN_00c9a810;
  uVar1 = *param_7;
  uVar2 = *param_8;
  *(undefined1 *)((long)puVar3 + lVar4 + 0x18) = 0x13;
  uVar5 = *param_3;
  uVar6 = *param_5;
  uVar7 = *param_6;
  uVar10 = param_4[1];
  uVar9 = *param_4;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x20) = *param_2;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x28) = uVar5;
  *(ushort *)((long)puVar3 + lVar4 + 0x19) =
       *(ushort *)((long)puVar3 + lVar4 + 0x19) & 0xf000 | 0x100;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x38) = uVar10;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x30) = uVar9;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x40) = uVar6;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x48) = uVar7;
  *(undefined4 *)((long)puVar3 + lVar4 + 0x50) = uVar1;
  *(undefined1 *)((long)puVar3 + lVar4 + 0x54) = uVar2;
  return;
}

~~~
