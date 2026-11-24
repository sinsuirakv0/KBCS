# 00bfaeac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfae10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfae10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-83609ba1a4cb0a8541a353c931587655)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfbea0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbea0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-59d9d9c6eac7d23d0cfa9f95feeb376d)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaeac",
  "name": "_ZNKSt6__ndk113random_device7entropyEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b3f1a54a1eb8f46069a89bcca62ecec5b9e95a8b7f64eaa4f098b64385926700",
  "source_text_sha256": "b3f1a54a1eb8f46069a89bcca62ecec5b9e95a8b7f64eaa4f098b64385926700",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaeac",
        "00bfaeff"
      ]
    ],
    "bytes_sha256": "364edbf14c90d0ef6dda70392994fab968fbec31c4aafec70553b9a8c762ef3a",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5e380](../00c5e/00c5e380.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 417 bytes

~~~c

undefined1  [16] _ZNKSt6__ndk113random_device7entropyEv(int *param_1)

{
  int iVar1;
  double dVar2;
  undefined1 auVar3 [16];
  uint local_14;
  
  iVar1 = ioctl(*param_1,0x80045200,&local_14);
  dVar2 = 0.0;
  if ((-1 < iVar1) && (-1 < (int)local_14)) {
    if (0x1f < local_14) {
      local_14 = 0x20;
    }
    dVar2 = (double)(int)local_14;
  }
  auVar3._8_8_ = 0;
  auVar3._0_8_ = dVar2;
  return auVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfaeac"></a> `00bfaeac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfaeb0"></a> `00bfaeb0` | `ff 83 00 d1` | sub sp,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfaeb4"></a> `00bfaeb4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaeb8"></a> `00bfaeb8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfaebc"></a> `00bfaebc` | `00 00 40 b9` | ldr w0,[x0] | `FALL_THROUGH`
<a id="insn-00bfaec0"></a> `00bfaec0` | `01 40 8a 52` | mov w1,#0x5200 | `FALL_THROUGH`
<a id="insn-00bfaec4"></a> `00bfaec4` | `a2 13 00 d1` | sub x2,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfaec8"></a> `00bfaec8` | `81 00 b0 72` | movk w1,#0x8004, LSL #16 | `FALL_THROUGH`
<a id="insn-00bfaecc"></a> `00bfaecc` | `2d 8d 01 94` | bl 0x00c5e380 | `UNCONDITIONAL_CALL`
<a id="insn-00bfaed0"></a> `00bfaed0` | `00 e4 00 2f` | movi d0,#0x0 | `FALL_THROUGH`
<a id="insn-00bfaed4"></a> `00bfaed4` | `e0 00 f8 37` | tbnz w0,#0x1f,0x00bfaef0 | `CONDITIONAL_JUMP`
<a id="insn-00bfaed8"></a> `00bfaed8` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfaedc"></a> `00bfaedc` | `a8 00 f8 37` | tbnz w8,#0x1f,0x00bfaef0 | `CONDITIONAL_JUMP`
<a id="insn-00bfaee0"></a> `00bfaee0` | `1f 81 00 71` | cmp w8,#0x20 | `FALL_THROUGH`
<a id="insn-00bfaee4"></a> `00bfaee4` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bfaee8"></a> `00bfaee8` | `08 31 89 1a` | csel w8,w8,w9,cc | `FALL_THROUGH`
<a id="insn-00bfaeec"></a> `00bfaeec` | `00 01 62 1e` | scvtf d0,w8 | `FALL_THROUGH`
<a id="insn-00bfaef0"></a> `00bfaef0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaef4"></a> `00bfaef4` | `ff 83 00 91` | add sp,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfaef8"></a> `00bfaef8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfaefc"></a> `00bfaefc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfaeac`](#insn-00bfaeac) 範囲 `[['00bfaeac', '00bfaed7']]`
  - `CONDITIONAL_JUMP` [`00bfaed4`](#insn-00bfaed4) → [`00bfaef0`](#insn-00bfaef0)
  - `FALL_THROUGH` [`00bfaed4`](#insn-00bfaed4) → [`00bfaed8`](#insn-00bfaed8)
- ブロック [`00bfaed8`](#insn-00bfaed8) 範囲 `[['00bfaed8', '00bfaedf']]`
  - `CONDITIONAL_JUMP` [`00bfaedc`](#insn-00bfaedc) → [`00bfaef0`](#insn-00bfaef0)
  - `FALL_THROUGH` [`00bfaedc`](#insn-00bfaedc) → [`00bfaee0`](#insn-00bfaee0)
- ブロック [`00bfaee0`](#insn-00bfaee0) 範囲 `[['00bfaee0', '00bfaeef']]`
  - `FALL_THROUGH` [`00bfaeec`](#insn-00bfaeec) → [`00bfaef0`](#insn-00bfaef0)
- ブロック [`00bfaef0`](#insn-00bfaef0) 範囲 `[['00bfaef0', '00bfaeff']]`

## 命令位置別の参照

- [`00bfaeb4`](#insn-00bfaeb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaecc`](#insn-00bfaecc) → [`00c5e380`](../00c5e/00c5e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e380` · 推定シンボル `None` · 推定型 `None`
- [`00bfaed4`](#insn-00bfaed4) → [`00bfaef0`](#insn-00bfaef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaed8`](#insn-00bfaed8) → `Stack[-0x14]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaedc`](#insn-00bfaedc) → [`00bfaef0`](#insn-00bfaef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaef0`](#insn-00bfaef0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfaeb4`](#insn-00bfaeb4)

~~~json
{
  "source": "00bfaeb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaecc`](#insn-00bfaecc)

~~~json
{
  "source": "00bfaecc",
  "target": "00c5e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfaed4`](#insn-00bfaed4)

~~~json
{
  "source": "00bfaed4",
  "target": "00bfaef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaed8`](#insn-00bfaed8)

~~~json
{
  "source": "00bfaed8",
  "target": "Stack[-0x14]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaedc`](#insn-00bfaedc)

~~~json
{
  "source": "00bfaedc",
  "target": "00bfaef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaef0`](#insn-00bfaef0)

~~~json
{
  "source": "00bfaef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
