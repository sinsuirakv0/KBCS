# 00c4edac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00c4edac",
  "name": "FUN_00c4edac",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f3dbbdb49cb666cfbd75f2bd7c861913fda7d2bda95e922e7c0246989d3161ec",
  "source_text_sha256": "f3dbbdb49cb666cfbd75f2bd7c861913fda7d2bda95e922e7c0246989d3161ec"
}
~~~

## 呼び出し元

- [00c3ad68](../00c3a/00c3ad68.md)

## 呼び出し先

- [00c580f0](../00c58/00c580f0.md)
- [00c5a0f0](../00c5a/00c5a0f0.md)

## 疑似コード / UTF-8 1025 bytes

~~~c

void FUN_00c4edac(long param_1,undefined8 *param_2,undefined1 *param_3)

{
  undefined1 uVar1;
  undefined8 *puVar2;
  long lVar3;
  undefined8 uVar4;
  void *pvVar5;
  
  pvVar5 = *(void **)(param_1 + 0x1330);
  lVar3 = *(long *)((long)pvVar5 + 8);
  puVar2 = pvVar5;
  if (lVar3 - 0xfd0U < 0xfffffffffffff010) {
    puVar2 = malloc(0x1000);
    if (puVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar3 = 0;
    *puVar2 = pvVar5;
    puVar2[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar2;
  }
  *(long *)((long)puVar2 + 8) = lVar3 + 0x20;
  *(undefined ***)((long)puVar2 + lVar3 + 0x10) = &PTR_FUN_00c99ca0;
  uVar4 = *param_2;
  *(undefined1 *)((long)puVar2 + lVar3 + 0x18) = 0x20;
  uVar1 = *param_3;
  *(undefined8 *)((long)puVar2 + lVar3 + 0x20) = uVar4;
  *(ushort *)((long)puVar2 + lVar3 + 0x19) =
       *(ushort *)((long)puVar2 + lVar3 + 0x19) & 0xf000 | 0x540;
  *(undefined1 *)((long)puVar2 + lVar3 + 0x28) = uVar1;
  return;
}

~~~
