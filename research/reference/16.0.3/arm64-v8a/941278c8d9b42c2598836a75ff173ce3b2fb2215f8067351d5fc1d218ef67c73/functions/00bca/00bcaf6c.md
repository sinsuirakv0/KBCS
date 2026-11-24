# 00bcaf6c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc9f78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9f78.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-cb2ccf44748f22813e35cc1e8f022d99)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcaf6c",
  "name": "_ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b1394661667b48d43d4049ef2ad9660c6060fa0f88646ea5664d06d0eee4569b",
  "source_text_sha256": "b1394661667b48d43d4049ef2ad9660c6060fa0f88646ea5664d06d0eee4569b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcaf6c",
        "00bcafe7"
      ]
    ],
    "bytes_sha256": "443ec6ab136f37ad940eace25611268a1ba8b7cbfaf3492c4eda8e820f3a6be3",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5e9c0](../00c5e/00c5e9c0.md)

## 呼び出し先

- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5be90](../00c5b/00c5be90.md)
- [00c5bea0](../00c5b/00c5bea0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1236 bytes

~~~c

void _ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
               (long param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  
                    /* catch() { ... } // from try @ 00bcac44 with catch @ 00bcaf84
                       catch() { ... } // from try @ 00bcadfc with catch @ 00bcaf84 */
                    /* catch() { ... } // from try @ 00bcad4c with catch @ 00bcaf8c */
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = param_2;
  lVar1 = param_1 + 0x30;
  _ZN8firebase12FutureHandleC1ERKS0_(lVar1,param_3);
  (**(code **)(**(long **)(param_1 + 0x28) + 0x10))(*(long **)(param_1 + 0x28),lVar1);
  _ZN8firebase12FutureHandle6DetachEv(lVar1);
  plVar2 = *(long **)(param_1 + 0x28);
                    /* try { // try from 00bcafc4 to 00ccb03f has its CatchHandler @ 00bcafc4
                       catch() { ... } // from try @ 00bcafc4 with catch @ 00bcafc4
                       catch() { ... } // from try @ 00bcb094 with catch @ 00bcafc4
                       catch() { ... } // from try @ 00bcb174 with catch @ 00bcafc4 */
  if (plVar2 != (long *)0x0) {
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcaf6c"></a> `00bcaf6c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcaf70"></a> `00bcaf70` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcaf74"></a> `00bcaf74` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcaf78"></a> `00bcaf78` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcaf7c"></a> `00bcaf7c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcaf80"></a> `00bcaf80` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bcaf84"></a> `00bcaf84` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bcaf88"></a> `00bcaf88` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcaf8c"></a> `00bcaf8c` | `61 43 02 94` | bl 0x00c5bd10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaf90"></a> `00bcaf90` | `74 16 00 f9` | str x20,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcaf94"></a> `00bcaf94` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bcaf98"></a> `00bcaf98` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcaf9c"></a> `00bcaf9c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcafa0"></a> `00bcafa0` | `c0 43 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcafa4"></a> `00bcafa4` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcafa8"></a> `00bcafa8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcafac"></a> `00bcafac` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bcafb0"></a> `00bcafb0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcafb4"></a> `00bcafb4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcafb8"></a> `00bcafb8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcafbc"></a> `00bcafbc` | `b5 43 02 94` | bl 0x00c5be90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcafc0"></a> `00bcafc0` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcafc4"></a> `00bcafc4` | `a0 00 00 b4` | cbz x0,0x00bcafd8 | `CONDITIONAL_JUMP`
<a id="insn-00bcafc8"></a> `00bcafc8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcafcc"></a> `00bcafcc` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bcafd0"></a> `00bcafd0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcafd4"></a> `00bcafd4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcafd8"></a> `00bcafd8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcafdc"></a> `00bcafdc` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcafe0"></a> `00bcafe0` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcafe4"></a> `00bcafe4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcaf6c`](#insn-00bcaf6c) 範囲 `[['00bcaf6c', '00bcaf83']]`
  - `FALL_THROUGH` [`00bcaf80`](#insn-00bcaf80) → [`00bcaf84`](#insn-00bcaf84)
- ブロック [`00bcaf84`](#insn-00bcaf84) 範囲 `[['00bcaf84', '00bcaf8b']]`
  - `FALL_THROUGH` [`00bcaf88`](#insn-00bcaf88) → [`00bcaf8c`](#insn-00bcaf8c)
- ブロック [`00bcaf8c`](#insn-00bcaf8c) 範囲 `[['00bcaf8c', '00bcafc3']]`
  - `FALL_THROUGH` [`00bcafc0`](#insn-00bcafc0) → [`00bcafc4`](#insn-00bcafc4)
- ブロック [`00bcafc4`](#insn-00bcafc4) 範囲 `[['00bcafc4', '00bcafc7']]`
  - `CONDITIONAL_JUMP` [`00bcafc4`](#insn-00bcafc4) → [`00bcafd8`](#insn-00bcafd8)
  - `FALL_THROUGH` [`00bcafc4`](#insn-00bcafc4) → [`00bcafc8`](#insn-00bcafc8)
- ブロック [`00bcafc8`](#insn-00bcafc8) 範囲 `[['00bcafc8', '00bcafd7']]`
  - `FALL_THROUGH` [`00bcafd4`](#insn-00bcafd4) → [`00bcafd8`](#insn-00bcafd8)
- ブロック [`00bcafd8`](#insn-00bcafd8) 範囲 `[['00bcafd8', '00bcafe7']]`

## 命令位置別の参照

- [`00bcaf6c`](#insn-00bcaf6c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf70`](#insn-00bcaf70) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf74`](#insn-00bcaf74) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf8c`](#insn-00bcaf8c) → [`00c5bd10`](../00c5b/00c5bd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd10` · 推定シンボル `None` · 推定型 `None`
- [`00bcafa0`](#insn-00bcafa0) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bcafbc`](#insn-00bcafbc) → [`00c5be90`](../00c5b/00c5be90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be90` · 推定シンボル `None` · 推定型 `None`
- [`00bcafc4`](#insn-00bcafc4) → [`00bcafd8`](#insn-00bcafd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafd8`](#insn-00bcafd8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafdc`](#insn-00bcafdc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcaf6c`](#insn-00bcaf6c)

~~~json
{
  "source": "00bcaf6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf70`](#insn-00bcaf70)

~~~json
{
  "source": "00bcaf70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf74`](#insn-00bcaf74)

~~~json
{
  "source": "00bcaf74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf8c`](#insn-00bcaf8c)

~~~json
{
  "source": "00bcaf8c",
  "target": "00c5bd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcafa0`](#insn-00bcafa0)

~~~json
{
  "source": "00bcafa0",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcafbc`](#insn-00bcafbc)

~~~json
{
  "source": "00bcafbc",
  "target": "00c5be90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcafc4`](#insn-00bcafc4)

~~~json
{
  "source": "00bcafc4",
  "target": "00bcafd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafd8`](#insn-00bcafd8)

~~~json
{
  "source": "00bcafd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafdc`](#insn-00bcafdc)

~~~json
{
  "source": "00bcafdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
