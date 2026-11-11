# 00b7fcfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b7fcfc",
  "name": "_ZN11flatbuffers21FlatBufferBuilderImplILb0EE11StartVectorINS_6OffsetEjEEvmmm",
  "size": 320,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "526006b91b89406afc295c7d8c7af69d6ee7ee30e9fa9551bb5e303c623eb7fa",
  "source_text_sha256": "526006b91b89406afc295c7d8c7af69d6ee7ee30e9fa9551bb5e303c623eb7fa"
}
~~~

## 呼び出し元

- [00c5c280](../00c5c/00c5c280.md)

## 呼び出し先

- [00c5c1a0](../00c5c/00c5c1a0.md)

## 疑似コード / UTF-8 2062 bytes

~~~c

void _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11StartVectorINS_6OffsetEjEEvmmm
               (long param_1,long param_2,long param_3,ulong param_4)

{
  ulong uVar1;
  int iVar2;
  uint uVar3;
  ulong uVar4;
  long lVar5;
  
  param_3 = param_3 * param_2;
  *(undefined1 *)(param_1 + 0x60) = 1;
  if (param_3 != 0) {
    if (*(ulong *)(param_1 + 0x68) < 4) {
      *(undefined8 *)(param_1 + 0x68) = 4;
    }
    iVar2 = *(int *)(param_1 + 0x30);
    uVar3 = -((int)param_3 + iVar2);
    uVar1 = (ulong)uVar3 & 3;
    if ((uVar3 & 3) != 0) {
      lVar5 = *(long *)(param_1 + 0x40);
      if ((uint)((int)lVar5 - *(int *)(param_1 + 0x48)) < uVar1) {
        _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar1);
        lVar5 = *(long *)(param_1 + 0x40);
        iVar2 = *(int *)(param_1 + 0x30);
      }
      *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar5 - uVar1);
      *(int *)(param_1 + 0x30) = iVar2 + (int)uVar1;
      *(undefined1 *)(lVar5 - uVar1) = 0;
      if (uVar1 != 1) {
        uVar4 = 1;
        do {
          *(undefined1 *)(*(long *)(param_1 + 0x40) + uVar4) = 0;
          uVar4 = uVar4 + 1;
        } while (uVar1 != uVar4);
      }
    }
    if (*(ulong *)(param_1 + 0x68) < param_4) {
      *(ulong *)(param_1 + 0x68) = param_4;
    }
    uVar3 = *(uint *)(param_1 + 0x30);
    uVar1 = param_4 - 1 & -(param_3 + (ulong)uVar3);
    if (uVar1 != 0) {
      lVar5 = *(long *)(param_1 + 0x40);
      if ((uint)((int)lVar5 - *(int *)(param_1 + 0x48)) < uVar1) {
        _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar1);
        lVar5 = *(long *)(param_1 + 0x40);
        uVar3 = *(uint *)(param_1 + 0x30);
      }
      *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar5 - uVar1);
      *(uint *)(param_1 + 0x30) = uVar3 + (int)uVar1;
      *(undefined1 *)(lVar5 - uVar1) = 0;
      if (uVar1 != 1) {
        uVar4 = 1;
        do {
          *(undefined1 *)(*(long *)(param_1 + 0x40) + uVar4) = 0;
          uVar4 = uVar4 + 1;
        } while (uVar1 != uVar4);
      }
    }
  }
  return;
}

~~~
