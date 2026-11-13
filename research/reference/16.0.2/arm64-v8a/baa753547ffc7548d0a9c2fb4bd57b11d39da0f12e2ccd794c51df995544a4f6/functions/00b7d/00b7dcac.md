# 00b7dcac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00b7dcac",
  "name": "_ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementItEEvtT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "81f44ac56998c5297aaea3df53421b1da72a53fcdf0fcd45d5a454c71044343b",
  "source_text_sha256": "81f44ac56998c5297aaea3df53421b1da72a53fcdf0fcd45d5a454c71044343b"
}
~~~

## 呼び出し元

- [00c5c2d0](../00c5c/00c5c2d0.md)

## 呼び出し先

- [00c5c270](../00c5c/00c5c270.md)

## 疑似コード / UTF-8 1741 bytes

~~~c

void _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementItEEvtT_
               (long param_1,uint param_2,undefined2 param_3)

{
  int iVar1;
  uint uVar2;
  ulong *puVar3;
  long lVar4;
  ulong uVar5;
  
  if (*(ulong *)(param_1 + 0x68) < 2) {
    *(undefined8 *)(param_1 + 0x68) = 2;
  }
  uVar2 = *(uint *)(param_1 + 0x30);
  uVar5 = (ulong)uVar2 & 1;
  if ((int)uVar5 != 0) {
    lVar4 = *(long *)(param_1 + 0x40);
    if ((uint)((int)lVar4 - *(int *)(param_1 + 0x48)) < uVar5) {
      _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar5);
      lVar4 = *(long *)(param_1 + 0x40);
      uVar2 = *(uint *)(param_1 + 0x30);
    }
    *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar4 - uVar5);
    *(uint *)(param_1 + 0x30) = uVar2 + (int)uVar5;
    *(undefined1 *)(lVar4 - uVar5) = 0;
  }
  lVar4 = *(long *)(param_1 + 0x40);
  puVar3 = *(ulong **)(param_1 + 0x48);
  if (((int)lVar4 - (int)puVar3 & 0xfffffffeU) == 0) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,2);
    lVar4 = *(long *)(param_1 + 0x40);
    puVar3 = *(ulong **)(param_1 + 0x48);
  }
  *(long *)(param_1 + 0x40) = lVar4 + -2;
  iVar1 = *(int *)(param_1 + 0x30) + 2;
  *(int *)(param_1 + 0x30) = iVar1;
  *(undefined2 *)(lVar4 + -2) = param_3;
  if (((int)(lVar4 + -2) - (int)puVar3 & 0xfffffff8U) == 0) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,8);
    puVar3 = *(ulong **)(param_1 + 0x48);
  }
  *puVar3 = CONCAT44(param_2,iVar1) & 0xffffffffffff;
  *(long *)(param_1 + 0x48) = *(long *)(param_1 + 0x48) + 8;
  *(int *)(param_1 + 0x50) = *(int *)(param_1 + 0x50) + 1;
  if ((uint)*(ushort *)(param_1 + 0x54) < (param_2 & 0xffff)) {
    *(short *)(param_1 + 0x54) = (short)param_2;
  }
  return;
}

~~~
