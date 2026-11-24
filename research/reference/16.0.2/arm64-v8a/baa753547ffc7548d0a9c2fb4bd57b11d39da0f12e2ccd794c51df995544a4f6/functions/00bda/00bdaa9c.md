# 00bdaa9c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdaa00`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bdaa00.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-80136b0fe66f254012d308ae01a71618)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdba90`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdba90.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-70ded1af0a2406fc256b15bd9447b575)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaa9c",
  "name": "_ZN8firebase4auth17PhoneAuthProvider8ListenerD2Ev",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42a6e64f7caf4588f45e8cc16694a9e6c4937499e9b7d92ce0ae99b28d595879",
  "source_text_sha256": "42a6e64f7caf4588f45e8cc16694a9e6c4937499e9b7d92ce0ae99b28d595879",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdaa9c",
        "00bdab2b"
      ]
    ],
    "bytes_sha256": "18667ccb095f551c8186aa750f0e360c0c4d1e30b69729617965ca9b3d8a0efc",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00574d2c](../00574/00574d2c.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5b330](../00c5b/00c5b330.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 614 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider8ListenerD2Ev(long *param_1)

{
  long lVar1;
  long *plVar2;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth17PhoneAuthProvider8ListenerE_00c9bb10 + 0x10);
  lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
  if (lVar1 == 0) {
    _ZN8firebase9LogAssertEPKcz("app != nullptr");
  }
  plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
  FUN_00574d2c(plVar2,*(undefined8 *)param_1[1],DAT_01126dc8);
  (**(code **)(*plVar2 + 0xb0))(plVar2,*(undefined8 *)param_1[1]);
  if ((void *)param_1[1] != (void *)0x0) {
    _ZdlPv((void *)param_1[1]);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdaa9c"></a> `00bdaa9c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdaaa0"></a> `00bdaaa0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaaa4"></a> `00bdaaa4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdaaa8"></a> `00bdaaa8` | `08 06 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdaaac"></a> `00bdaaac` | `08 89 45 f9` | ldr x8,[x8, #0xb10] | `FALL_THROUGH`
<a id="insn-00bdaab0"></a> `00bdaab0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdaab4"></a> `00bdaab4` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bdaab8"></a> `00bdaab8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdaabc"></a> `00bdaabc` | `1d 02 02 94` | bl 0x00c5b330 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaac0"></a> `00bdaac0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdaac4"></a> `00bdaac4` | `80 00 00 b5` | cbnz x0,0x00bdaad4 | `CONDITIONAL_JUMP`
<a id="insn-00bdaac8"></a> `00bdaac8` | `c0 b6 ff 90` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bdaacc"></a> `00bdaacc` | `00 24 18 91` | add x0,x0,#0x609 | `FALL_THROUGH`
<a id="insn-00bdaad0"></a> `00bdaad0` | `80 01 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaad4"></a> `00bdaad4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdaad8"></a> `00bdaad8` | `9e 01 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaadc"></a> `00bdaadc` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bdaae0"></a> `00bdaae0` | `69 2a 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdaae4"></a> `00bdaae4` | `22 e5 46 f9` | ldr x2,[x9, #0xdc8] | `FALL_THROUGH`
<a id="insn-00bdaae8"></a> `00bdaae8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdaaec"></a> `00bdaaec` | `01 01 40 f9` | ldr x1,[x8] | `FALL_THROUGH`
<a id="insn-00bdaaf0"></a> `00bdaaf0` | `8f 68 e6 97` | bl 0x00574d2c | `UNCONDITIONAL_CALL`
<a id="insn-00bdaaf4"></a> `00bdaaf4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bdaaf8"></a> `00bdaaf8` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bdaafc"></a> `00bdaafc` | `01 01 40 f9` | ldr x1,[x8] | `FALL_THROUGH`
<a id="insn-00bdab00"></a> `00bdab00` | `28 59 40 f9` | ldr x8,[x9, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdab04"></a> `00bdab04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdab08"></a> `00bdab08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdab0c"></a> `00bdab0c` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bdab10"></a> `00bdab10` | `80 00 00 b4` | cbz x0,0x00bdab20 | `CONDITIONAL_JUMP`
<a id="insn-00bdab14"></a> `00bdab14` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdab18"></a> `00bdab18` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdab1c"></a> `00bdab1c` | `19 f5 01 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00bdab20"></a> `00bdab20` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdab24"></a> `00bdab24` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdab28"></a> `00bdab28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdaa9c`](#insn-00bdaa9c) 範囲 `[['00bdaa9c', '00bdaac7']]`
  - `CONDITIONAL_JUMP` [`00bdaac4`](#insn-00bdaac4) → [`00bdaad4`](#insn-00bdaad4)
  - `FALL_THROUGH` [`00bdaac4`](#insn-00bdaac4) → [`00bdaac8`](#insn-00bdaac8)
- ブロック [`00bdaac8`](#insn-00bdaac8) 範囲 `[['00bdaac8', '00bdaad3']]`
  - `FALL_THROUGH` [`00bdaad0`](#insn-00bdaad0) → [`00bdaad4`](#insn-00bdaad4)
- ブロック [`00bdaad4`](#insn-00bdaad4) 範囲 `[['00bdaad4', '00bdab13']]`
  - `CONDITIONAL_JUMP` [`00bdab10`](#insn-00bdab10) → [`00bdab20`](#insn-00bdab20)
  - `FALL_THROUGH` [`00bdab10`](#insn-00bdab10) → [`00bdab14`](#insn-00bdab14)
- ブロック [`00bdab14`](#insn-00bdab14) 範囲 `[['00bdab14', '00bdab1f']]`
- ブロック [`00bdab20`](#insn-00bdab20) 範囲 `[['00bdab20', '00bdab2b']]`

## 命令位置別の参照

- [`00bdaa9c`](#insn-00bdaa9c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaaa0`](#insn-00bdaaa0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaaac`](#insn-00bdaaac) → `00c9bb10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdaab8`](#insn-00bdaab8) → `00c92610`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[64]`
- [`00bdaabc`](#insn-00bdaabc) → [`00c5b330`](../00c5b/00c5b330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b330` · 推定シンボル `None` · 推定型 `None`
- [`00bdaac4`](#insn-00bdaac4) → [`00bdaad4`](#insn-00bdaad4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaacc`](#insn-00bdaacc) → `002b2609`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdaad0`](#insn-00bdaad0) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bdaad8`](#insn-00bdaad8) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bdaae4`](#insn-00bdaae4) → `01126dc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdaaf0`](#insn-00bdaaf0) → [`00574d2c`](../00574/00574d2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574d2c` · 推定シンボル `None` · 推定型 `None`
- [`00bdab10`](#insn-00bdab10) → [`00bdab20`](#insn-00bdab20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab14`](#insn-00bdab14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab1c`](#insn-00bdab1c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bdab20`](#insn-00bdab20) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdaa9c`](#insn-00bdaa9c)

~~~json
{
  "source": "00bdaa9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaaa0`](#insn-00bdaaa0)

~~~json
{
  "source": "00bdaaa0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaaac`](#insn-00bdaaac)

~~~json
{
  "source": "00bdaaac",
  "target": "00c9bb10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bb10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdaab8`](#insn-00bdaab8)

~~~json
{
  "source": "00bdaab8",
  "target": "00c92610",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92600",
  "offset": 16,
  "size": 64,
  "datatype": "undefined1[64]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdaabc`](#insn-00bdaabc)

~~~json
{
  "source": "00bdaabc",
  "target": "00c5b330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaac4`](#insn-00bdaac4)

~~~json
{
  "source": "00bdaac4",
  "target": "00bdaad4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaacc`](#insn-00bdaacc)

~~~json
{
  "source": "00bdaacc",
  "target": "002b2609",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2609",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2609",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdaad0`](#insn-00bdaad0)

~~~json
{
  "source": "00bdaad0",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaad8`](#insn-00bdaad8)

~~~json
{
  "source": "00bdaad8",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaae4`](#insn-00bdaae4)

~~~json
{
  "source": "00bdaae4",
  "target": "01126dc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126dc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdaaf0`](#insn-00bdaaf0)

~~~json
{
  "source": "00bdaaf0",
  "target": "00574d2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdab10`](#insn-00bdab10)

~~~json
{
  "source": "00bdab10",
  "target": "00bdab20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab14`](#insn-00bdab14)

~~~json
{
  "source": "00bdab14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab1c`](#insn-00bdab1c)

~~~json
{
  "source": "00bdab1c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdab20`](#insn-00bdab20)

~~~json
{
  "source": "00bdab20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
