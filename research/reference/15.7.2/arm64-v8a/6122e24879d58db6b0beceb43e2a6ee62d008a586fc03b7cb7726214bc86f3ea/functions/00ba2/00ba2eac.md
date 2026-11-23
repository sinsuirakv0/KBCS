# 00ba2eac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ba2f74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2f74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0077.md#compare-53afb3afe88bb3061ad5549f4e93cad3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba2eac",
  "name": "FUN_00ba2eac",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac9baa97a4c2a525c0ecf350946a5cd087d3aef723b8492644a48531ea4e403d",
  "source_text_sha256": "ac9baa97a4c2a525c0ecf350946a5cd087d3aef723b8492644a48531ea4e403d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba2eac",
        "00ba2fa7"
      ]
    ],
    "bytes_sha256": "7d523e3d31b5b78e492130b61b64748910391beaa9b95e9a5629d9cb20fc6064",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00ba2510](../00ba2/00ba2510.md)
- [00ba49ac](../00ba4/00ba49ac.md)

## 呼び出し先

- [00bb8ac8](../00bb8/00bb8ac8.md)
- [00bd6d60](../00bd6/00bd6d60.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00be0de0](../00be0/00be0de0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1282 bytes

~~~c

void FUN_00ba2eac(long param_1,long param_2)

{
  undefined *puVar1;
  ulong uVar2;
  long lVar3;
  ulong uVar4;
  long *plVar5;
  long *plVar6;
  ulong uVar7;
  undefined *local_48;
  undefined8 **local_40;
  undefined **local_38;
  
  puVar1 = PTR__ZNSt6__ndk15ctypeIcE2idE_00c1ad40;
  local_48 = PTR__ZNSt6__ndk15ctypeIcE2idE_00c1ad40;
  if (*(long *)PTR__ZNSt6__ndk15ctypeIcE2idE_00c1ad40 != -1) {
    local_38 = &local_48;
    local_40 = &local_38;
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk15ctypeIcE2idE_00c1ad40,&local_40,FUN_00bb903c);
  }
  uVar2 = (ulong)*(int *)(puVar1 + 8);
  uVar7 = uVar2 - 1;
  FUN_00bd6d60(1,param_2 + 8);
  plVar5 = (long *)(param_1 + 0x10);
  lVar3 = *plVar5;
  uVar4 = *(long *)(param_1 + 0x18) - lVar3 >> 3;
  if (uVar4 <= uVar7) {
    if (uVar2 < uVar4 || uVar2 - uVar4 == 0) {
      if (uVar2 < uVar4) {
        *(ulong *)(param_1 + 0x18) = lVar3 + uVar2 * 8;
      }
    }
    else {
      FUN_00bb8ac8(plVar5,uVar2 - uVar4);
      lVar3 = *plVar5;
    }
  }
  plVar6 = *(long **)(lVar3 + uVar7 * 8);
  if ((plVar6 != (long *)0x0) && (lVar3 = FUN_00bd6d90(0xffffffffffffffff,plVar6 + 1), lVar3 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
  }
  *(long *)(*plVar5 + uVar7 * 8) = param_2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba2eac"></a> `00ba2eac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00ba2eb0"></a> `00ba2eb0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ba2eb4"></a> `00ba2eb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba2eb8"></a> `00ba2eb8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba2ebc"></a> `00ba2ebc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba2ec0"></a> `00ba2ec0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ba2ec4"></a> `00ba2ec4` | `d4 03 00 90` | adrp x20,0xc1a000 | `FALL_THROUGH`
<a id="insn-00ba2ec8"></a> `00ba2ec8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00ba2ecc"></a> `00ba2ecc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ba2ed0"></a> `00ba2ed0` | `94 a2 46 f9` | ldr x20,[x20, #0xd40] | `FALL_THROUGH`
<a id="insn-00ba2ed4"></a> `00ba2ed4` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba2ed8"></a> `00ba2ed8` | `88 fe df c8` | ldar x8,[x20] | `FALL_THROUGH`
<a id="insn-00ba2edc"></a> `00ba2edc` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba2ee0"></a> `00ba2ee0` | `60 01 00 54` | b.eq 0x00ba2f0c | `CONDITIONAL_JUMP`
<a id="insn-00ba2ee4"></a> `00ba2ee4` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ba2ee8"></a> `00ba2ee8` | `a9 23 00 d1` | sub x9,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00ba2eec"></a> `00ba2eec` | `c0 03 00 90` | adrp x0,0xc1a000 | `FALL_THROUGH`
<a id="insn-00ba2ef0"></a> `00ba2ef0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ba2ef4"></a> `00ba2ef4` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00ba2ef8"></a> `00ba2ef8` | `22 0a 0b 10` | adr x2,0xbb903c | `FALL_THROUGH`
<a id="insn-00ba2efc"></a> `00ba2efc` | `e9 0b 00 f9` | str x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba2f00"></a> `00ba2f00` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ba2f04"></a> `00ba2f04` | `00 a0 46 f9` | ldr x0,[x0, #0xd40] | `FALL_THROUGH`
<a id="insn-00ba2f08"></a> `00ba2f08` | `b6 f7 00 94` | bl 0x00be0de0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba2f0c"></a> `00ba2f0c` | `88 0a 80 b9` | ldrsw x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00ba2f10"></a> `00ba2f10` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00ba2f14"></a> `00ba2f14` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ba2f18"></a> `00ba2f18` | `16 05 00 d1` | sub x22,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba2f1c"></a> `00ba2f1c` | `91 cf 00 94` | bl 0x00bd6d60 | `UNCONDITIONAL_CALL`
<a id="insn-00ba2f20"></a> `00ba2f20` | `f4 03 15 aa` | mov x20,x21 | `FALL_THROUGH`
<a id="insn-00ba2f24"></a> `00ba2f24` | `88 26 c1 a9` | ldp x8,x9,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00ba2f28"></a> `00ba2f28` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00ba2f2c"></a> `00ba2f2c` | `2a fd 43 93` | asr x10,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00ba2f30"></a> `00ba2f30` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00ba2f34"></a> `00ba2f34` | `68 01 00 54` | b.hi 0x00ba2f60 | `CONDITIONAL_JUMP`
<a id="insn-00ba2f38"></a> `00ba2f38` | `c9 06 00 91` | add x9,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00ba2f3c"></a> `00ba2f3c` | `21 01 0a eb` | subs x1,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba2f40"></a> `00ba2f40` | `a9 00 00 54` | b.ls 0x00ba2f54 | `CONDITIONAL_JUMP`
<a id="insn-00ba2f44"></a> `00ba2f44` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ba2f48"></a> `00ba2f48` | `e0 56 00 94` | bl 0x00bb8ac8 | `UNCONDITIONAL_CALL`
<a id="insn-00ba2f4c"></a> `00ba2f4c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ba2f50"></a> `00ba2f50` | `04 00 00 14` | b 0x00ba2f60 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba2f54"></a> `00ba2f54` | `62 00 00 54` | b.cs 0x00ba2f60 | `CONDITIONAL_JUMP`
<a id="insn-00ba2f58"></a> `00ba2f58` | `09 0d 09 8b` | add x9,x8,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00ba2f5c"></a> `00ba2f5c` | `a9 0e 00 f9` | str x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00ba2f60"></a> `00ba2f60` | `15 79 76 f8` | ldr x21,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00ba2f64"></a> `00ba2f64` | `35 01 00 b4` | cbz x21,0x00ba2f88 | `CONDITIONAL_JUMP`
<a id="insn-00ba2f68"></a> `00ba2f68` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00ba2f6c"></a> `00ba2f6c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ba2f70"></a> `00ba2f70` | `88 cf 00 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ba2f74"></a> `00ba2f74` | `a0 00 00 b5` | cbnz x0,0x00ba2f88 | `CONDITIONAL_JUMP`
<a id="insn-00ba2f78"></a> `00ba2f78` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00ba2f7c"></a> `00ba2f7c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ba2f80"></a> `00ba2f80` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ba2f84"></a> `00ba2f84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ba2f88"></a> `00ba2f88` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ba2f8c"></a> `00ba2f8c` | `13 79 36 f8` | str x19,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00ba2f90"></a> `00ba2f90` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba2f94"></a> `00ba2f94` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba2f98"></a> `00ba2f98` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba2f9c"></a> `00ba2f9c` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ba2fa0"></a> `00ba2fa0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00ba2fa4"></a> `00ba2fa4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba2eac`](#insn-00ba2eac) 範囲 `[['00ba2eac', '00ba2ee3']]`
  - `CONDITIONAL_JUMP` [`00ba2ee0`](#insn-00ba2ee0) → [`00ba2f0c`](#insn-00ba2f0c)
  - `FALL_THROUGH` [`00ba2ee0`](#insn-00ba2ee0) → [`00ba2ee4`](#insn-00ba2ee4)
- ブロック [`00ba2ee4`](#insn-00ba2ee4) 範囲 `[['00ba2ee4', '00ba2f0b']]`
  - `FALL_THROUGH` [`00ba2f08`](#insn-00ba2f08) → [`00ba2f0c`](#insn-00ba2f0c)
- ブロック [`00ba2f0c`](#insn-00ba2f0c) 範囲 `[['00ba2f0c', '00ba2f37']]`
  - `CONDITIONAL_JUMP` [`00ba2f34`](#insn-00ba2f34) → [`00ba2f60`](#insn-00ba2f60)
  - `FALL_THROUGH` [`00ba2f34`](#insn-00ba2f34) → [`00ba2f38`](#insn-00ba2f38)
- ブロック [`00ba2f38`](#insn-00ba2f38) 範囲 `[['00ba2f38', '00ba2f43']]`
  - `CONDITIONAL_JUMP` [`00ba2f40`](#insn-00ba2f40) → [`00ba2f54`](#insn-00ba2f54)
  - `FALL_THROUGH` [`00ba2f40`](#insn-00ba2f40) → [`00ba2f44`](#insn-00ba2f44)
- ブロック [`00ba2f44`](#insn-00ba2f44) 範囲 `[['00ba2f44', '00ba2f53']]`
  - `UNCONDITIONAL_JUMP` [`00ba2f50`](#insn-00ba2f50) → [`00ba2f60`](#insn-00ba2f60)
- ブロック [`00ba2f54`](#insn-00ba2f54) 範囲 `[['00ba2f54', '00ba2f57']]`
  - `CONDITIONAL_JUMP` [`00ba2f54`](#insn-00ba2f54) → [`00ba2f60`](#insn-00ba2f60)
  - `FALL_THROUGH` [`00ba2f54`](#insn-00ba2f54) → [`00ba2f58`](#insn-00ba2f58)
- ブロック [`00ba2f58`](#insn-00ba2f58) 範囲 `[['00ba2f58', '00ba2f5f']]`
  - `FALL_THROUGH` [`00ba2f5c`](#insn-00ba2f5c) → [`00ba2f60`](#insn-00ba2f60)
- ブロック [`00ba2f60`](#insn-00ba2f60) 範囲 `[['00ba2f60', '00ba2f67']]`
  - `CONDITIONAL_JUMP` [`00ba2f64`](#insn-00ba2f64) → [`00ba2f88`](#insn-00ba2f88)
  - `FALL_THROUGH` [`00ba2f64`](#insn-00ba2f64) → [`00ba2f68`](#insn-00ba2f68)
- ブロック [`00ba2f68`](#insn-00ba2f68) 範囲 `[['00ba2f68', '00ba2f77']]`
  - `CONDITIONAL_JUMP` [`00ba2f74`](#insn-00ba2f74) → [`00ba2f88`](#insn-00ba2f88)
  - `FALL_THROUGH` [`00ba2f74`](#insn-00ba2f74) → [`00ba2f78`](#insn-00ba2f78)
- ブロック [`00ba2f78`](#insn-00ba2f78) 範囲 `[['00ba2f78', '00ba2f87']]`
  - `FALL_THROUGH` [`00ba2f84`](#insn-00ba2f84) → [`00ba2f88`](#insn-00ba2f88)
- ブロック [`00ba2f88`](#insn-00ba2f88) 範囲 `[['00ba2f88', '00ba2fa7']]`

## 命令位置別の参照

- [`00ba2eb4`](#insn-00ba2eb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2eb8`](#insn-00ba2eb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ebc`](#insn-00ba2ebc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ed0`](#insn-00ba2ed0) → `00c1ad40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba2ed4`](#insn-00ba2ed4) → `010a2a10`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00ba2ed4`](#insn-00ba2ed4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ed8`](#insn-00ba2ed8) → `010a2a10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00ba2ee0`](#insn-00ba2ee0) → [`00ba2f0c`](#insn-00ba2f0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ef0`](#insn-00ba2ef0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ef8`](#insn-00ba2ef8) → [`00bb903c`](../00bb9/00bb903c.md) · `PARAM` · `ANALYSIS` · 関数 `00bb903c` · 推定シンボル `None` · 推定型 `None`
- [`00ba2efc`](#insn-00ba2efc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f04`](#insn-00ba2f04) → `00c1ad40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba2f04`](#insn-00ba2f04) → `010a2a10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00ba2f08`](#insn-00ba2f08) → [`00be0de0`](../00be0/00be0de0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0de0` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f0c`](#insn-00ba2f0c) → `010a2a18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00ba2f1c`](#insn-00ba2f1c) → [`00bd6d60`](../00bd6/00bd6d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d60` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f34`](#insn-00ba2f34) → [`00ba2f60`](#insn-00ba2f60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f40`](#insn-00ba2f40) → [`00ba2f54`](#insn-00ba2f54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f48`](#insn-00ba2f48) → [`00bb8ac8`](../00bb8/00bb8ac8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bb8ac8` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f50`](#insn-00ba2f50) → [`00ba2f60`](#insn-00ba2f60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f54`](#insn-00ba2f54) → [`00ba2f60`](#insn-00ba2f60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f64`](#insn-00ba2f64) → [`00ba2f88`](#insn-00ba2f88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f70`](#insn-00ba2f70) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f74`](#insn-00ba2f74) → [`00ba2f88`](#insn-00ba2f88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f90`](#insn-00ba2f90) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f94`](#insn-00ba2f94) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f98`](#insn-00ba2f98) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba2eb4`](#insn-00ba2eb4)

~~~json
{
  "source": "00ba2eb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2eb8`](#insn-00ba2eb8)

~~~json
{
  "source": "00ba2eb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ebc`](#insn-00ba2ebc)

~~~json
{
  "source": "00ba2ebc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ed0`](#insn-00ba2ed0)

~~~json
{
  "source": "00ba2ed0",
  "target": "00c1ad40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ad40",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ba2ed4`](#insn-00ba2ed4)

~~~json
{
  "source": "00ba2ed4",
  "target": "010a2a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2a10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba2ed4`](#insn-00ba2ed4)

~~~json
{
  "source": "00ba2ed4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ed8`](#insn-00ba2ed8)

~~~json
{
  "source": "00ba2ed8",
  "target": "010a2a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2a10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba2ee0`](#insn-00ba2ee0)

~~~json
{
  "source": "00ba2ee0",
  "target": "00ba2f0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ef0`](#insn-00ba2ef0)

~~~json
{
  "source": "00ba2ef0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ef8`](#insn-00ba2ef8)

~~~json
{
  "source": "00ba2ef8",
  "target": "00bb903c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2efc`](#insn-00ba2efc)

~~~json
{
  "source": "00ba2efc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f04`](#insn-00ba2f04)

~~~json
{
  "source": "00ba2f04",
  "target": "00c1ad40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ad40",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ba2f04`](#insn-00ba2f04)

~~~json
{
  "source": "00ba2f04",
  "target": "010a2a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2a10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba2f08`](#insn-00ba2f08)

~~~json
{
  "source": "00ba2f08",
  "target": "00be0de0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2f0c`](#insn-00ba2f0c)

~~~json
{
  "source": "00ba2f0c",
  "target": "010a2a18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2a18",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba2f1c`](#insn-00ba2f1c)

~~~json
{
  "source": "00ba2f1c",
  "target": "00bd6d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2f34`](#insn-00ba2f34)

~~~json
{
  "source": "00ba2f34",
  "target": "00ba2f60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f40`](#insn-00ba2f40)

~~~json
{
  "source": "00ba2f40",
  "target": "00ba2f54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f48`](#insn-00ba2f48)

~~~json
{
  "source": "00ba2f48",
  "target": "00bb8ac8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2f50`](#insn-00ba2f50)

~~~json
{
  "source": "00ba2f50",
  "target": "00ba2f60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f54`](#insn-00ba2f54)

~~~json
{
  "source": "00ba2f54",
  "target": "00ba2f60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f64`](#insn-00ba2f64)

~~~json
{
  "source": "00ba2f64",
  "target": "00ba2f88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f70`](#insn-00ba2f70)

~~~json
{
  "source": "00ba2f70",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2f74`](#insn-00ba2f74)

~~~json
{
  "source": "00ba2f74",
  "target": "00ba2f88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f90`](#insn-00ba2f90)

~~~json
{
  "source": "00ba2f90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f94`](#insn-00ba2f94)

~~~json
{
  "source": "00ba2f94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f98`](#insn-00ba2f98)

~~~json
{
  "source": "00ba2f98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
