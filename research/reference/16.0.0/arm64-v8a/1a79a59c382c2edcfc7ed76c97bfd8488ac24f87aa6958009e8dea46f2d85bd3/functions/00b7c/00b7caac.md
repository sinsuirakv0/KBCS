# 00b7caac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b7caac",
  "name": "_ZN11flatbuffers6Parser15SerializeStructERNS_21FlatBufferBuilderImplILb0EEERKNS_9StructDefERKNS_5ValueE",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f4d03e5e51dec5feb81e84bb4aacf1803be0a86ab825d91e73877611621b76b",
  "source_text_sha256": "9f4d03e5e51dec5feb81e84bb4aacf1803be0a86ab825d91e73877611621b76b"
}
~~~

## 呼び出し元

- [00c5c1c0](../00c5c/00c5c1c0.md)

## 呼び出し先

- [00c57c00](../00c57/00c57c00.md)
- [00c5bda0](../00c5b/00c5bda0.md)

## 疑似コード / UTF-8 3041 bytes

~~~c

void _ZN11flatbuffers6Parser15SerializeStructERNS_21FlatBufferBuilderImplILb0EEERKNS_9StructDefERKNS_5ValueE
               (undefined8 param_1,long param_2,long param_3,long param_4)

{
  undefined4 uVar1;
  ushort uVar2;
  uint uVar3;
  ulong uVar4;
  ulong *puVar5;
  ulong uVar6;
  long lVar7;
  void *__src;
  
  uVar6 = *(ulong *)(param_3 + 0xd8);
  if (*(ulong *)(param_2 + 0x68) < uVar6) {
    *(ulong *)(param_2 + 0x68) = uVar6;
  }
                    /* try { // try from 00b7cadc to 00c7cae3 has its CatchHandler @ 00b7d7fc */
  uVar3 = *(uint *)(param_2 + 0x30);
  uVar6 = uVar6 - 1 & -(ulong)uVar3;
  if (uVar6 != 0) {
    lVar7 = *(long *)(param_2 + 0x40);
    if ((uint)((int)lVar7 - *(int *)(param_2 + 0x48)) < uVar6) {
      _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_2,uVar6);
      lVar7 = *(long *)(param_2 + 0x40);
      uVar3 = *(uint *)(param_2 + 0x30);
    }
    *(undefined1 **)(param_2 + 0x40) = (undefined1 *)(lVar7 - uVar6);
    *(uint *)(param_2 + 0x30) = uVar3 + (int)uVar6;
                    /* try { // try from 00b7cb2c to 00c7cb37 has its CatchHandler @ 00b7d7e8 */
    *(undefined1 *)(lVar7 - uVar6) = 0;
    if (uVar6 != 1) {
      uVar4 = 1;
      do {
                    /* try { // try from 00b7cb38 to 00c7cb4b has its CatchHandler @ 00b7d7d8 */
        *(undefined1 *)(*(long *)(param_2 + 0x40) + uVar4) = 0;
        uVar4 = uVar4 + 1;
      } while (uVar6 != uVar4);
    }
  }
                    /* try { // try from 00b7cb4c to 00c7cb57 has its CatchHandler @ 00b7d7a8 */
  if ((*(byte *)(param_4 + 0x20) & 1) == 0) {
    __src = (void *)(param_4 + 0x21);
                    /* try { // try from 00b7cb5c to 00c7cb73 has its CatchHandler @ 00b7d754 */
    uVar6 = *(ulong *)(param_3 + 0xe0);
  }
  else {
    __src = *(void **)(param_4 + 0x30);
    uVar6 = *(ulong *)(param_3 + 0xe0);
  }
  if (uVar6 != 0) {
    lVar7 = *(long *)(param_2 + 0x40);
                    /* try { // try from 00b7cb78 to 00c7cb8f has its CatchHandler @ 00b7d744 */
    if ((uint)((int)lVar7 - *(int *)(param_2 + 0x48)) < uVar6) {
                    /* try { // try from 00b7cb90 to 00c7cc57 has its CatchHandler @ 00b7c2fc */
      _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_2,uVar6);
      lVar7 = *(long *)(param_2 + 0x40);
    }
    *(void **)(param_2 + 0x40) = (void *)(lVar7 - uVar6);
    *(int *)(param_2 + 0x30) = *(int *)(param_2 + 0x30) + (int)uVar6;
    memcpy((void *)(lVar7 - uVar6),__src,uVar6);
  }
  puVar5 = *(ulong **)(param_2 + 0x48);
  uVar2 = *(ushort *)(param_4 + 0x38);
  uVar1 = *(undefined4 *)(param_2 + 0x30);
  if ((*(int *)(param_2 + 0x40) - (int)puVar5 & 0xfffffff8U) == 0) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_2,8);
    puVar5 = *(ulong **)(param_2 + 0x48);
  }
  *puVar5 = (ulong)CONCAT24(uVar2,uVar1);
  *(long *)(param_2 + 0x48) = *(long *)(param_2 + 0x48) + 8;
  *(int *)(param_2 + 0x50) = *(int *)(param_2 + 0x50) + 1;
  if (*(ushort *)(param_2 + 0x54) < uVar2) {
    *(ushort *)(param_2 + 0x54) = uVar2;
  }
  return;
}

~~~
