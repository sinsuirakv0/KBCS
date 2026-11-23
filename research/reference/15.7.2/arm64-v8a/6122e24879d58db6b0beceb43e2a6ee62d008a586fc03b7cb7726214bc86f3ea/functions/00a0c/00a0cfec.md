# 00a0cfec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a0cfec`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0cfec.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0018.md#compare-7ad6fc248216a690bf3696fe781f067f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a0cfec",
  "name": "FUN_00a0cfec",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9b15a2ec88979455a3a5d97a02868cec721a190d8d4ff553cfc002be1d38588a",
  "source_text_sha256": "9b15a2ec88979455a3a5d97a02868cec721a190d8d4ff553cfc002be1d38588a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a0cfec",
        "00a0d06b"
      ]
    ],
    "bytes_sha256": "1591ee0603facf25c74ab325c567d4ed8bd7285078b37955e89ba67acf1f4cda",
    "instruction_count": 32,
    "instruction_bytes": 128,
    "body_bytes": 128,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006eccf4](../006ec/006eccf4.md)
- [009f4a74](../009f4/009f4a74.md)

## 呼び出し先

- [00a0cdf4](../00a0c/00a0cdf4.md)
- [00a0e088](../00a0e/00a0e088.md)
- [00a0e40c](../00a0e/00a0e40c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 714 bytes

~~~c

void FUN_00a0cfec(long param_1,undefined4 param_2,undefined8 param_3,undefined8 param_4,
                 undefined8 param_5)

{
  int iVar1;
  
                    /* try { // try from 00a0d008 to 00b0d00f has its CatchHandler @ 00a0d41c */
                    /* try { // try from 00a0d010 to 00b0d663 has its CatchHandler @ 00a0a31c */
  FUN_00a0e40c(*(undefined8 *)(param_1 + 0x70),*(undefined4 *)(param_1 + 0x7c));
  iVar1 = FUN_00a0e088();
  if (iVar1 == 0) {
    iVar1 = FUN_00a0cdf4(param_1,param_2,param_3,param_4,param_5);
  }
  else {
    iVar1 = 0;
  }
  iVar1 = *(int *)(param_1 + 0x88) + iVar1;
  if (0x3b9ac9fe < iVar1) {
    iVar1 = 999999999;
  }
  *(int *)(param_1 + 0x88) = iVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a0cfec"></a> `00a0cfec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00a0cff0"></a> `00a0cff0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a0cff4"></a> `00a0cff4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a0cff8"></a> `00a0cff8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a0cffc"></a> `00a0cffc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a0d000"></a> `00a0d000` | `00 38 40 f9` | ldr x0,[x0, #0x70] | `FALL_THROUGH`
<a id="insn-00a0d004"></a> `00a0d004` | `f6 03 01 2a` | mov w22,w1 | `FALL_THROUGH`
<a id="insn-00a0d008"></a> `00a0d008` | `68 7e 40 b9` | ldr w8,[x19, #0x7c] | `FALL_THROUGH`
<a id="insn-00a0d00c"></a> `00a0d00c` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00a0d010"></a> `00a0d010` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00a0d014"></a> `00a0d014` | `e1 03 08 2a` | mov w1,w8 | `FALL_THROUGH`
<a id="insn-00a0d018"></a> `00a0d018` | `fd 04 00 94` | bl 0x00a0e40c | `UNCONDITIONAL_CALL`
<a id="insn-00a0d01c"></a> `00a0d01c` | `1b 04 00 94` | bl 0x00a0e088 | `UNCONDITIONAL_CALL`
<a id="insn-00a0d020"></a> `00a0d020` | `60 00 00 34` | cbz w0,0x00a0d02c | `CONDITIONAL_JUMP`
<a id="insn-00a0d024"></a> `00a0d024` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a0d028"></a> `00a0d028` | `06 00 00 14` | b 0x00a0d040 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0d02c"></a> `00a0d02c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a0d030"></a> `00a0d030` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-00a0d034"></a> `00a0d034` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00a0d038"></a> `00a0d038` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-00a0d03c"></a> `00a0d03c` | `6e ff ff 97` | bl 0x00a0cdf4 | `UNCONDITIONAL_CALL`
<a id="insn-00a0d040"></a> `00a0d040` | `68 8a 40 b9` | ldr w8,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00a0d044"></a> `00a0d044` | `e9 3f 99 52` | mov w9,#0xc9ff | `FALL_THROUGH`
<a id="insn-00a0d048"></a> `00a0d048` | `49 73 a7 72` | movk w9,#0x3b9a, LSL #16 | `FALL_THROUGH`
<a id="insn-00a0d04c"></a> `00a0d04c` | `08 01 00 0b` | add w8,w8,w0 | `FALL_THROUGH`
<a id="insn-00a0d050"></a> `00a0d050` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00a0d054"></a> `00a0d054` | `08 b1 89 1a` | csel w8,w8,w9,lt | `FALL_THROUGH`
<a id="insn-00a0d058"></a> `00a0d058` | `68 8a 00 b9` | str w8,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00a0d05c"></a> `00a0d05c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a0d060"></a> `00a0d060` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a0d064"></a> `00a0d064` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a0d068"></a> `00a0d068` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a0cfec`](#insn-00a0cfec) 範囲 `[['00a0cfec', '00a0d007']]`
  - `FALL_THROUGH` [`00a0d004`](#insn-00a0d004) → [`00a0d008`](#insn-00a0d008)
- ブロック [`00a0d008`](#insn-00a0d008) 範囲 `[['00a0d008', '00a0d00f']]`
  - `FALL_THROUGH` [`00a0d00c`](#insn-00a0d00c) → [`00a0d010`](#insn-00a0d010)
- ブロック [`00a0d010`](#insn-00a0d010) 範囲 `[['00a0d010', '00a0d023']]`
  - `CONDITIONAL_JUMP` [`00a0d020`](#insn-00a0d020) → [`00a0d02c`](#insn-00a0d02c)
  - `FALL_THROUGH` [`00a0d020`](#insn-00a0d020) → [`00a0d024`](#insn-00a0d024)
- ブロック [`00a0d024`](#insn-00a0d024) 範囲 `[['00a0d024', '00a0d02b']]`
  - `UNCONDITIONAL_JUMP` [`00a0d028`](#insn-00a0d028) → [`00a0d040`](#insn-00a0d040)
- ブロック [`00a0d02c`](#insn-00a0d02c) 範囲 `[['00a0d02c', '00a0d03f']]`
  - `FALL_THROUGH` [`00a0d03c`](#insn-00a0d03c) → [`00a0d040`](#insn-00a0d040)
- ブロック [`00a0d040`](#insn-00a0d040) 範囲 `[['00a0d040', '00a0d06b']]`

## 命令位置別の参照

- [`00a0cfec`](#insn-00a0cfec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0cff0`](#insn-00a0cff0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0cff4`](#insn-00a0cff4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0d018`](#insn-00a0d018) → [`00a0e40c`](../00a0e/00a0e40c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a0e40c` · 推定シンボル `None` · 推定型 `None`
- [`00a0d01c`](#insn-00a0d01c) → [`00a0e088`](../00a0e/00a0e088.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a0e088` · 推定シンボル `None` · 推定型 `None`
- [`00a0d020`](#insn-00a0d020) → [`00a0d02c`](#insn-00a0d02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0d028`](#insn-00a0d028) → [`00a0d040`](#insn-00a0d040) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0d03c`](#insn-00a0d03c) → [`00a0cdf4`](00a0cdf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a0cdf4` · 推定シンボル `None` · 推定型 `None`
- [`00a0d05c`](#insn-00a0d05c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0d060`](#insn-00a0d060) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0d064`](#insn-00a0d064) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a0cfec`](#insn-00a0cfec)

~~~json
{
  "source": "00a0cfec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0cff0`](#insn-00a0cff0)

~~~json
{
  "source": "00a0cff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0cff4`](#insn-00a0cff4)

~~~json
{
  "source": "00a0cff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0d018`](#insn-00a0d018)

~~~json
{
  "source": "00a0d018",
  "target": "00a0e40c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0d01c`](#insn-00a0d01c)

~~~json
{
  "source": "00a0d01c",
  "target": "00a0e088",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0d020`](#insn-00a0d020)

~~~json
{
  "source": "00a0d020",
  "target": "00a0d02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0d028`](#insn-00a0d028)

~~~json
{
  "source": "00a0d028",
  "target": "00a0d040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0d03c`](#insn-00a0d03c)

~~~json
{
  "source": "00a0d03c",
  "target": "00a0cdf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0d05c`](#insn-00a0d05c)

~~~json
{
  "source": "00a0d05c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0d060`](#insn-00a0d060)

~~~json
{
  "source": "00a0d060",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0d064`](#insn-00a0d064)

~~~json
{
  "source": "00a0d064",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
