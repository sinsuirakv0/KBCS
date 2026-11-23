# 00b0ecdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b0eda4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0eda4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-97237e6beb0604d2a37474ce70fdbbdb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0ecdc",
  "name": "_ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96cafc98461b2d9e58eda77306b8d3bc611b5a3f0735c90a4fed86aef0530462",
  "source_text_sha256": "96cafc98461b2d9e58eda77306b8d3bc611b5a3f0735c90a4fed86aef0530462",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0ecdc",
        "00b0edbb"
      ]
    ],
    "bytes_sha256": "654fc579963a54e4f669f3dfa640cef3d56d9b36367af7cb7e14c5a0e3fe52fd",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdb160](../00bdb/00bdb160.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bde1c0](../00bde/00bde1c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1329 bytes

~~~c

void _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
               (ulong *param_1,char *param_2,byte *param_3)

{
  ulong uVar1;
  byte bVar2;
  size_t __n;
  byte *pbVar3;
  void *__dest;
  ulong uVar4;
  
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  __n = strlen(param_2);
  bVar2 = *param_3;
  uVar1 = (ulong)(bVar2 >> 1);
  if ((bVar2 & 1) != 0) {
    uVar1 = *(ulong *)(param_3 + 8);
  }
  uVar4 = uVar1 + __n;
  if (uVar4 < 0xfffffffffffffff0) {
    if (uVar4 < 0x17) {
      __dest = (void *)((long)param_1 + 1);
      *(char *)param_1 = (char)((int)__n << 1);
    }
    else {
      uVar4 = uVar4 + 0x10 & 0xfffffffffffffff0;
                    /* catch() { ... } // from try @ 00b0ebec with catch @ 00b0ed58 */
      __dest = (void *)_Znwm(uVar4);
      param_1[1] = __n;
      param_1[2] = (ulong)__dest;
      *param_1 = uVar4 | 1;
    }
    if (__n != 0) {
      memcpy(__dest,param_2,__n);
    }
    *(undefined1 *)((long)__dest + __n) = 0;
    pbVar3 = *(byte **)(param_3 + 0x10);
    if ((bVar2 & 1) == 0) {
      pbVar3 = param_3 + 1;
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
              (param_1,pbVar3,uVar1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0ecdc"></a> `00b0ecdc` | `fa 67 bb a9` | stp x26,x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00b0ece0"></a> `00b0ece0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ece4"></a> `00b0ece4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0ece8"></a> `00b0ece8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0ecec"></a> `00b0ecec` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b0ecf0"></a> `00b0ecf0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b0ecf4"></a> `00b0ecf4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b0ecf8"></a> `00b0ecf8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b0ecfc"></a> `00b0ecfc` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00b0ed00"></a> `00b0ed00` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00b0ed04"></a> `00b0ed04` | `1f 09 00 f9` | str xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ed08"></a> `00b0ed08` | `e2 30 03 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ed0c"></a> `00b0ed0c` | `7a 02 40 39` | ldrb w26,[x19] | `FALL_THROUGH`
<a id="insn-00b0ed10"></a> `00b0ed10` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b0ed14"></a> `00b0ed14` | `49 ff 41 d3` | lsr x9,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00b0ed18"></a> `00b0ed18` | `5f 03 00 72` | tst w26,#0x1 | `FALL_THROUGH`
<a id="insn-00b0ed1c"></a> `00b0ed1c` | `37 01 88 9a` | csel x23,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00b0ed20"></a> `00b0ed20` | `e8 02 00 8b` | add x8,x23,x0 | `FALL_THROUGH`
<a id="insn-00b0ed24"></a> `00b0ed24` | `1f 41 00 b1` | cmn x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b0ed28"></a> `00b0ed28` | `82 04 00 54` | b.cs 0x00b0edb8 | `CONDITIONAL_JUMP`
<a id="insn-00b0ed2c"></a> `00b0ed2c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b0ed30"></a> `00b0ed30` | `1f 59 00 f1` | cmp x8,#0x16 | `FALL_THROUGH`
<a id="insn-00b0ed34"></a> `00b0ed34` | `e8 00 00 54` | b.hi 0x00b0ed50 | `CONDITIONAL_JUMP`
<a id="insn-00b0ed38"></a> `00b0ed38` | `c8 7a 1f 53` | lsl w8,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00b0ed3c"></a> `00b0ed3c` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00b0ed40"></a> `00b0ed40` | `08 17 00 38` | strb w8,[x24], #0x1 | `FALL_THROUGH`
<a id="insn-00b0ed44"></a> `00b0ed44` | `59 03 00 12` | and w25,w26,#0x1 | `FALL_THROUGH`
<a id="insn-00b0ed48"></a> `00b0ed48` | `96 01 00 b5` | cbnz x22,0x00b0ed78 | `CONDITIONAL_JUMP`
<a id="insn-00b0ed4c"></a> `00b0ed4c` | `0f 00 00 14` | b 0x00b0ed88 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0ed50"></a> `00b0ed50` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b0ed54"></a> `00b0ed54` | `19 ed 7c 92` | and x25,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00b0ed58"></a> `00b0ed58` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00b0ed5c"></a> `00b0ed5c` | `79 30 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ed60"></a> `00b0ed60` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00b0ed64"></a> `00b0ed64` | `28 03 40 b2` | orr x8,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00b0ed68"></a> `00b0ed68` | `96 82 00 a9` | stp x22,x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b0ed6c"></a> `00b0ed6c` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00b0ed70"></a> `00b0ed70` | `59 03 00 12` | and w25,w26,#0x1 | `FALL_THROUGH`
<a id="insn-00b0ed74"></a> `00b0ed74` | `b6 00 00 b4` | cbz x22,0x00b0ed88 | `CONDITIONAL_JUMP`
<a id="insn-00b0ed78"></a> `00b0ed78` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b0ed7c"></a> `00b0ed7c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b0ed80"></a> `00b0ed80` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b0ed84"></a> `00b0ed84` | `cb 30 03 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ed88"></a> `00b0ed88` | `1f 6b 36 38` | strb wzr,[x24, x22, LSL ] | `FALL_THROUGH`
<a id="insn-00b0ed8c"></a> `00b0ed8c` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ed90"></a> `00b0ed90` | `3f 03 00 71` | cmp w25,#0x0 | `FALL_THROUGH`
<a id="insn-00b0ed94"></a> `00b0ed94` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ed98"></a> `00b0ed98` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00b0ed9c"></a> `00b0ed9c` | `01 15 93 9a` | csinc x1,x8,x19,ne | `FALL_THROUGH`
<a id="insn-00b0eda0"></a> `00b0eda0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b0eda4"></a> `00b0eda4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0eda8"></a> `00b0eda8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0edac"></a> `00b0edac` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0edb0"></a> `00b0edb0` | `fa 67 c5 a8` | ldp x26,x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00b0edb4"></a> `00b0edb4` | `9f 30 03 14` | b 0x00bdb030 | `CALL_TERMINATOR`
<a id="insn-00b0edb8"></a> `00b0edb8` | `02 3d 03 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0ecdc`](#insn-00b0ecdc) 範囲 `[['00b0ecdc', '00b0ed2b']]`
  - `CONDITIONAL_JUMP` [`00b0ed28`](#insn-00b0ed28) → [`00b0edb8`](#insn-00b0edb8)
  - `FALL_THROUGH` [`00b0ed28`](#insn-00b0ed28) → [`00b0ed2c`](#insn-00b0ed2c)
- ブロック [`00b0ed2c`](#insn-00b0ed2c) 範囲 `[['00b0ed2c', '00b0ed37']]`
  - `CONDITIONAL_JUMP` [`00b0ed34`](#insn-00b0ed34) → [`00b0ed50`](#insn-00b0ed50)
  - `FALL_THROUGH` [`00b0ed34`](#insn-00b0ed34) → [`00b0ed38`](#insn-00b0ed38)
- ブロック [`00b0ed38`](#insn-00b0ed38) 範囲 `[['00b0ed38', '00b0ed4b']]`
  - `CONDITIONAL_JUMP` [`00b0ed48`](#insn-00b0ed48) → [`00b0ed78`](#insn-00b0ed78)
  - `FALL_THROUGH` [`00b0ed48`](#insn-00b0ed48) → [`00b0ed4c`](#insn-00b0ed4c)
- ブロック [`00b0ed4c`](#insn-00b0ed4c) 範囲 `[['00b0ed4c', '00b0ed4f']]`
  - `UNCONDITIONAL_JUMP` [`00b0ed4c`](#insn-00b0ed4c) → [`00b0ed88`](#insn-00b0ed88)
- ブロック [`00b0ed50`](#insn-00b0ed50) 範囲 `[['00b0ed50', '00b0ed57']]`
  - `FALL_THROUGH` [`00b0ed54`](#insn-00b0ed54) → [`00b0ed58`](#insn-00b0ed58)
- ブロック [`00b0ed58`](#insn-00b0ed58) 範囲 `[['00b0ed58', '00b0ed77']]`
  - `CONDITIONAL_JUMP` [`00b0ed74`](#insn-00b0ed74) → [`00b0ed88`](#insn-00b0ed88)
  - `FALL_THROUGH` [`00b0ed74`](#insn-00b0ed74) → [`00b0ed78`](#insn-00b0ed78)
- ブロック [`00b0ed78`](#insn-00b0ed78) 範囲 `[['00b0ed78', '00b0ed87']]`
  - `FALL_THROUGH` [`00b0ed84`](#insn-00b0ed84) → [`00b0ed88`](#insn-00b0ed88)
- ブロック [`00b0ed88`](#insn-00b0ed88) 範囲 `[['00b0ed88', '00b0edb7']]`
- ブロック [`00b0edb8`](#insn-00b0edb8) 範囲 `[['00b0edb8', '00b0edbb']]`

## 命令位置別の参照

- [`00b0ecdc`](#insn-00b0ecdc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ece0`](#insn-00b0ece0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ece4`](#insn-00b0ece4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ece8`](#insn-00b0ece8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ecec`](#insn-00b0ecec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ed08`](#insn-00b0ed08) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b0ed28`](#insn-00b0ed28) → [`00b0edb8`](#insn-00b0edb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ed34`](#insn-00b0ed34) → [`00b0ed50`](#insn-00b0ed50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ed48`](#insn-00b0ed48) → [`00b0ed78`](#insn-00b0ed78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ed4c`](#insn-00b0ed4c) → [`00b0ed88`](#insn-00b0ed88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ed5c`](#insn-00b0ed5c) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00b0ed74`](#insn-00b0ed74) → [`00b0ed88`](#insn-00b0ed88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ed84`](#insn-00b0ed84) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00b0eda0`](#insn-00b0eda0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0eda4`](#insn-00b0eda4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0eda8`](#insn-00b0eda8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0edac`](#insn-00b0edac) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0edb4`](#insn-00b0edb4) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00b0edb8`](#insn-00b0edb8) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0ecdc`](#insn-00b0ecdc)

~~~json
{
  "source": "00b0ecdc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ece0`](#insn-00b0ece0)

~~~json
{
  "source": "00b0ece0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ece4`](#insn-00b0ece4)

~~~json
{
  "source": "00b0ece4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ece8`](#insn-00b0ece8)

~~~json
{
  "source": "00b0ece8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ecec`](#insn-00b0ecec)

~~~json
{
  "source": "00b0ecec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ed08`](#insn-00b0ed08)

~~~json
{
  "source": "00b0ed08",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ed28`](#insn-00b0ed28)

~~~json
{
  "source": "00b0ed28",
  "target": "00b0edb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ed34`](#insn-00b0ed34)

~~~json
{
  "source": "00b0ed34",
  "target": "00b0ed50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ed48`](#insn-00b0ed48)

~~~json
{
  "source": "00b0ed48",
  "target": "00b0ed78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ed4c`](#insn-00b0ed4c)

~~~json
{
  "source": "00b0ed4c",
  "target": "00b0ed88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ed5c`](#insn-00b0ed5c)

~~~json
{
  "source": "00b0ed5c",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ed74`](#insn-00b0ed74)

~~~json
{
  "source": "00b0ed74",
  "target": "00b0ed88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ed84`](#insn-00b0ed84)

~~~json
{
  "source": "00b0ed84",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0eda0`](#insn-00b0eda0)

~~~json
{
  "source": "00b0eda0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0eda4`](#insn-00b0eda4)

~~~json
{
  "source": "00b0eda4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0eda8`](#insn-00b0eda8)

~~~json
{
  "source": "00b0eda8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0edac`](#insn-00b0edac)

~~~json
{
  "source": "00b0edac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0edb4`](#insn-00b0edb4)

~~~json
{
  "source": "00b0edb4",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0edb8`](#insn-00b0edb8)

~~~json
{
  "source": "00b0edb8",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
