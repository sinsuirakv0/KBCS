# 00aff3ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aff2e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff2e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-84754858e4ec74fb21c9fc0e3d1a8436)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aff3f0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff3f0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-4e76bba76d884ec508aae094b633755d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aff3ac",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c8f2b9e76245a92640bc8a89ff7af82762c46eedf8000f8838409ff0371a3aa9",
  "source_text_sha256": "c8f2b9e76245a92640bc8a89ff7af82762c46eedf8000f8838409ff0371a3aa9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aff3ac",
        "00aff42f"
      ]
    ],
    "bytes_sha256": "96b36ae992cb5119114f2331ba1bce5502e92f708d7a0734932d871f7bb953d1",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bddfb0](../00bdd/00bddfb0.md)

## 呼び出し先

- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2805 bytes

~~~c

long _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(long param_1,ulong param_2)

{
  long *plVar1;
  long *plVar2;
  long lVar3;
  long *plVar4;
  
                    /* catch() { ... } // from try @ 00afceac with catch @ 00aff3ac */
                    /* catch() { ... } // from try @ 00afce7c with catch @ 00aff3b0 */
                    /* catch() { ... } // from try @ 00afcdc8 with catch @ 00aff3b8 */
                    /* catch() { ... } // from try @ 00afcd98 with catch @ 00aff3bc */
                    /* catch() { ... } // from try @ 00afcd68 with catch @ 00aff3c4 */
                    /* catch() { ... } // from try @ 00afccdc with catch @ 00aff3c8 */
                    /* catch() { ... } // from try @ 00afccac with catch @ 00aff3cc */
  _ZN8firebase5Mutex7AcquireEv(param_1 + 8);
  plVar4 = (long *)(param_1 + 0x38);
  plVar2 = (long *)*plVar4;
                    /* catch() { ... } // from try @ 00afcbf4 with catch @ 00aff3d4 */
  plVar1 = plVar4;
  if (plVar2 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00afcae8 with catch @ 00aff3dc */
                    /* catch() { ... } // from try @ 00afca2c with catch @ 00aff3e4 */
                    /* catch() { ... } // from try @ 00afc9fc with catch @ 00aff3e8 */
      if ((ulong)plVar2[4] >= param_2) {
        plVar1 = plVar2;
      }
      plVar2 = (long *)plVar2[(ulong)plVar2[4] < param_2];
                    /* catch() { ... } // from try @ 00afc9cc with catch @ 00aff3f0 */
    } while (plVar2 != (long *)0x0);
                    /* catch() { ... } // from try @ 00afc934 with catch @ 00aff3f4 */
                    /* catch() { ... } // from try @ 00afbdd8 with catch @ 00aff3f8 */
    if ((plVar1 != plVar4) && ((ulong)plVar1[4] <= param_2)) {
                    /* catch() { ... } // from try @ 00afbc98 with catch @ 00aff410 */
      lVar3 = plVar1[5];
      goto LAB_00aff414;
    }
  }
                    /* catch() { ... } // from try @ 00afbd90 with catch @ 00aff408 */
  lVar3 = 0;
                    /* catch() { ... } // from try @ 00afbd40 with catch @ 00aff40c */
LAB_00aff414:
                    /* catch() { ... } // from try @ 00afbbfc with catch @ 00aff414 */
                    /* catch() { ... } // from try @ 00afbbcc with catch @ 00aff418 */
  _ZN8firebase5Mutex7ReleaseEv(param_1 + 8);
                    /* catch() { ... } // from try @ 00afbba0 with catch @ 00aff41c */
                    /* catch() { ... } // from try @ 00afbb70 with catch @ 00aff420 */
                    /* catch() { ... } // from try @ 00afbb30 with catch @ 00aff424 */
                    /* catch() { ... } // from try @ 00afbb00 with catch @ 00aff428 */
                    /* catch() { ... } // from try @ 00afbad4 with catch @ 00aff42c */
  return lVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aff3ac"></a> `00aff3ac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aff3b0"></a> `00aff3b0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aff3b4"></a> `00aff3b4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aff3b8"></a> `00aff3b8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aff3bc"></a> `00aff3bc` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00aff3c0"></a> `00aff3c0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aff3c4"></a> `00aff3c4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aff3c8"></a> `00aff3c8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00aff3cc"></a> `00aff3cc` | `01 7a 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00aff3d0"></a> `00aff3d0` | `a9 8e 43 f8` | ldr x9,[x21, #0x38]! | `FALL_THROUGH`
<a id="insn-00aff3d4"></a> `00aff3d4` | `a9 01 00 b4` | cbz x9,0x00aff408 | `CONDITIONAL_JUMP`
<a id="insn-00aff3d8"></a> `00aff3d8` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00aff3dc"></a> `00aff3dc` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00aff3e0"></a> `00aff3e0` | `5f 01 14 eb` | cmp x10,x20 | `FALL_THROUGH`
<a id="insn-00aff3e4"></a> `00aff3e4` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00aff3e8"></a> `00aff3e8` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00aff3ec"></a> `00aff3ec` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aff3f0"></a> `00aff3f0` | `69 ff ff b5` | cbnz x9,0x00aff3dc | `CONDITIONAL_JUMP`
<a id="insn-00aff3f4"></a> `00aff3f4` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00aff3f8"></a> `00aff3f8` | `80 00 00 54` | b.eq 0x00aff408 | `CONDITIONAL_JUMP`
<a id="insn-00aff3fc"></a> `00aff3fc` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aff400"></a> `00aff400` | `3f 01 14 eb` | cmp x9,x20 | `FALL_THROUGH`
<a id="insn-00aff404"></a> `00aff404` | `69 00 00 54` | b.ls 0x00aff410 | `CONDITIONAL_JUMP`
<a id="insn-00aff408"></a> `00aff408` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00aff40c"></a> `00aff40c` | `02 00 00 14` | b 0x00aff414 | `UNCONDITIONAL_JUMP`
<a id="insn-00aff410"></a> `00aff410` | `14 15 40 f9` | ldr x20,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aff414"></a> `00aff414` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aff418"></a> `00aff418` | `f2 79 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00aff41c"></a> `00aff41c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aff420"></a> `00aff420` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aff424"></a> `00aff424` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aff428"></a> `00aff428` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aff42c"></a> `00aff42c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aff3ac`](#insn-00aff3ac) 範囲 `[['00aff3ac', '00aff3af']]`
  - `FALL_THROUGH` [`00aff3ac`](#insn-00aff3ac) → [`00aff3b0`](#insn-00aff3b0)
- ブロック [`00aff3b0`](#insn-00aff3b0) 範囲 `[['00aff3b0', '00aff3b7']]`
  - `FALL_THROUGH` [`00aff3b4`](#insn-00aff3b4) → [`00aff3b8`](#insn-00aff3b8)
- ブロック [`00aff3b8`](#insn-00aff3b8) 範囲 `[['00aff3b8', '00aff3bb']]`
  - `FALL_THROUGH` [`00aff3b8`](#insn-00aff3b8) → [`00aff3bc`](#insn-00aff3bc)
- ブロック [`00aff3bc`](#insn-00aff3bc) 範囲 `[['00aff3bc', '00aff3c3']]`
  - `FALL_THROUGH` [`00aff3c0`](#insn-00aff3c0) → [`00aff3c4`](#insn-00aff3c4)
- ブロック [`00aff3c4`](#insn-00aff3c4) 範囲 `[['00aff3c4', '00aff3c7']]`
  - `FALL_THROUGH` [`00aff3c4`](#insn-00aff3c4) → [`00aff3c8`](#insn-00aff3c8)
- ブロック [`00aff3c8`](#insn-00aff3c8) 範囲 `[['00aff3c8', '00aff3cb']]`
  - `FALL_THROUGH` [`00aff3c8`](#insn-00aff3c8) → [`00aff3cc`](#insn-00aff3cc)
- ブロック [`00aff3cc`](#insn-00aff3cc) 範囲 `[['00aff3cc', '00aff3d3']]`
  - `FALL_THROUGH` [`00aff3d0`](#insn-00aff3d0) → [`00aff3d4`](#insn-00aff3d4)
- ブロック [`00aff3d4`](#insn-00aff3d4) 範囲 `[['00aff3d4', '00aff3d7']]`
  - `CONDITIONAL_JUMP` [`00aff3d4`](#insn-00aff3d4) → [`00aff408`](#insn-00aff408)
  - `FALL_THROUGH` [`00aff3d4`](#insn-00aff3d4) → [`00aff3d8`](#insn-00aff3d8)
- ブロック [`00aff3d8`](#insn-00aff3d8) 範囲 `[['00aff3d8', '00aff3db']]`
  - `FALL_THROUGH` [`00aff3d8`](#insn-00aff3d8) → [`00aff3dc`](#insn-00aff3dc)
- ブロック [`00aff3dc`](#insn-00aff3dc) 範囲 `[['00aff3dc', '00aff3e3']]`
  - `FALL_THROUGH` [`00aff3e0`](#insn-00aff3e0) → [`00aff3e4`](#insn-00aff3e4)
- ブロック [`00aff3e4`](#insn-00aff3e4) 範囲 `[['00aff3e4', '00aff3e7']]`
  - `FALL_THROUGH` [`00aff3e4`](#insn-00aff3e4) → [`00aff3e8`](#insn-00aff3e8)
- ブロック [`00aff3e8`](#insn-00aff3e8) 範囲 `[['00aff3e8', '00aff3ef']]`
  - `FALL_THROUGH` [`00aff3ec`](#insn-00aff3ec) → [`00aff3f0`](#insn-00aff3f0)
- ブロック [`00aff3f0`](#insn-00aff3f0) 範囲 `[['00aff3f0', '00aff3f3']]`
  - `CONDITIONAL_JUMP` [`00aff3f0`](#insn-00aff3f0) → [`00aff3dc`](#insn-00aff3dc)
  - `FALL_THROUGH` [`00aff3f0`](#insn-00aff3f0) → [`00aff3f4`](#insn-00aff3f4)
- ブロック [`00aff3f4`](#insn-00aff3f4) 範囲 `[['00aff3f4', '00aff3f7']]`
  - `FALL_THROUGH` [`00aff3f4`](#insn-00aff3f4) → [`00aff3f8`](#insn-00aff3f8)
- ブロック [`00aff3f8`](#insn-00aff3f8) 範囲 `[['00aff3f8', '00aff3fb']]`
  - `CONDITIONAL_JUMP` [`00aff3f8`](#insn-00aff3f8) → [`00aff408`](#insn-00aff408)
  - `FALL_THROUGH` [`00aff3f8`](#insn-00aff3f8) → [`00aff3fc`](#insn-00aff3fc)
- ブロック [`00aff3fc`](#insn-00aff3fc) 範囲 `[['00aff3fc', '00aff407']]`
  - `CONDITIONAL_JUMP` [`00aff404`](#insn-00aff404) → [`00aff410`](#insn-00aff410)
  - `FALL_THROUGH` [`00aff404`](#insn-00aff404) → [`00aff408`](#insn-00aff408)
- ブロック [`00aff408`](#insn-00aff408) 範囲 `[['00aff408', '00aff40b']]`
  - `FALL_THROUGH` [`00aff408`](#insn-00aff408) → [`00aff40c`](#insn-00aff40c)
- ブロック [`00aff40c`](#insn-00aff40c) 範囲 `[['00aff40c', '00aff40f']]`
  - `UNCONDITIONAL_JUMP` [`00aff40c`](#insn-00aff40c) → [`00aff414`](#insn-00aff414)
- ブロック [`00aff410`](#insn-00aff410) 範囲 `[['00aff410', '00aff413']]`
  - `FALL_THROUGH` [`00aff410`](#insn-00aff410) → [`00aff414`](#insn-00aff414)
- ブロック [`00aff414`](#insn-00aff414) 範囲 `[['00aff414', '00aff417']]`
  - `FALL_THROUGH` [`00aff414`](#insn-00aff414) → [`00aff418`](#insn-00aff418)
- ブロック [`00aff418`](#insn-00aff418) 範囲 `[['00aff418', '00aff41b']]`
  - `FALL_THROUGH` [`00aff418`](#insn-00aff418) → [`00aff41c`](#insn-00aff41c)
- ブロック [`00aff41c`](#insn-00aff41c) 範囲 `[['00aff41c', '00aff41f']]`
  - `FALL_THROUGH` [`00aff41c`](#insn-00aff41c) → [`00aff420`](#insn-00aff420)
- ブロック [`00aff420`](#insn-00aff420) 範囲 `[['00aff420', '00aff423']]`
  - `FALL_THROUGH` [`00aff420`](#insn-00aff420) → [`00aff424`](#insn-00aff424)
- ブロック [`00aff424`](#insn-00aff424) 範囲 `[['00aff424', '00aff427']]`
  - `FALL_THROUGH` [`00aff424`](#insn-00aff424) → [`00aff428`](#insn-00aff428)
- ブロック [`00aff428`](#insn-00aff428) 範囲 `[['00aff428', '00aff42b']]`
  - `FALL_THROUGH` [`00aff428`](#insn-00aff428) → [`00aff42c`](#insn-00aff42c)
- ブロック [`00aff42c`](#insn-00aff42c) 範囲 `[['00aff42c', '00aff42f']]`

## 命令位置別の参照

- [`00aff3ac`](#insn-00aff3ac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff3b0`](#insn-00aff3b0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff3b4`](#insn-00aff3b4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff3cc`](#insn-00aff3cc) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00aff3d4`](#insn-00aff3d4) → [`00aff408`](#insn-00aff408) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff3f0`](#insn-00aff3f0) → [`00aff3dc`](#insn-00aff3dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff3f8`](#insn-00aff3f8) → [`00aff408`](#insn-00aff408) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff404`](#insn-00aff404) → [`00aff410`](#insn-00aff410) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff40c`](#insn-00aff40c) → [`00aff414`](#insn-00aff414) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff418`](#insn-00aff418) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00aff420`](#insn-00aff420) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff424`](#insn-00aff424) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aff3ac`](#insn-00aff3ac)

~~~json
{
  "source": "00aff3ac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff3b0`](#insn-00aff3b0)

~~~json
{
  "source": "00aff3b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff3b4`](#insn-00aff3b4)

~~~json
{
  "source": "00aff3b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff3cc`](#insn-00aff3cc)

~~~json
{
  "source": "00aff3cc",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff3d4`](#insn-00aff3d4)

~~~json
{
  "source": "00aff3d4",
  "target": "00aff408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff3f0`](#insn-00aff3f0)

~~~json
{
  "source": "00aff3f0",
  "target": "00aff3dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff3f8`](#insn-00aff3f8)

~~~json
{
  "source": "00aff3f8",
  "target": "00aff408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff404`](#insn-00aff404)

~~~json
{
  "source": "00aff404",
  "target": "00aff410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff40c`](#insn-00aff40c)

~~~json
{
  "source": "00aff40c",
  "target": "00aff414",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff418`](#insn-00aff418)

~~~json
{
  "source": "00aff418",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff420`](#insn-00aff420)

~~~json
{
  "source": "00aff420",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff424`](#insn-00aff424)

~~~json
{
  "source": "00aff424",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
