# 00bfbea0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfaeac`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaeac.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-59d9d9c6eac7d23d0cfa9f95feeb376d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbea0",
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
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbea0",
        "00bfbef3"
      ]
    ],
    "bytes_sha256": "c7aa9f5c26ed3f662c01cc8112ad6f52015a61684a8863c08faf6049b2f9b61f",
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

- [00c5f350](../00c5f/00c5f350.md)

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
<a id="insn-00bfbea0"></a> `00bfbea0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbea4"></a> `00bfbea4` | `ff 83 00 d1` | sub sp,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfbea8"></a> `00bfbea8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbeac"></a> `00bfbeac` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfbeb0"></a> `00bfbeb0` | `00 00 40 b9` | ldr w0,[x0] | `FALL_THROUGH`
<a id="insn-00bfbeb4"></a> `00bfbeb4` | `01 40 8a 52` | mov w1,#0x5200 | `FALL_THROUGH`
<a id="insn-00bfbeb8"></a> `00bfbeb8` | `a2 13 00 d1` | sub x2,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfbebc"></a> `00bfbebc` | `81 00 b0 72` | movk w1,#0x8004, LSL #16 | `FALL_THROUGH`
<a id="insn-00bfbec0"></a> `00bfbec0` | `24 8d 01 94` | bl 0x00c5f350 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbec4"></a> `00bfbec4` | `00 e4 00 2f` | movi d0,#0x0 | `FALL_THROUGH`
<a id="insn-00bfbec8"></a> `00bfbec8` | `e0 00 f8 37` | tbnz w0,#0x1f,0x00bfbee4 | `CONDITIONAL_JUMP`
<a id="insn-00bfbecc"></a> `00bfbecc` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfbed0"></a> `00bfbed0` | `a8 00 f8 37` | tbnz w8,#0x1f,0x00bfbee4 | `CONDITIONAL_JUMP`
<a id="insn-00bfbed4"></a> `00bfbed4` | `1f 81 00 71` | cmp w8,#0x20 | `FALL_THROUGH`
<a id="insn-00bfbed8"></a> `00bfbed8` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bfbedc"></a> `00bfbedc` | `08 31 89 1a` | csel w8,w8,w9,cc | `FALL_THROUGH`
<a id="insn-00bfbee0"></a> `00bfbee0` | `00 01 62 1e` | scvtf d0,w8 | `FALL_THROUGH`
<a id="insn-00bfbee4"></a> `00bfbee4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbee8"></a> `00bfbee8` | `ff 83 00 91` | add sp,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfbeec"></a> `00bfbeec` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbef0"></a> `00bfbef0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbea0`](#insn-00bfbea0) 範囲 `[['00bfbea0', '00bfbecb']]`
  - `CONDITIONAL_JUMP` [`00bfbec8`](#insn-00bfbec8) → [`00bfbee4`](#insn-00bfbee4)
  - `FALL_THROUGH` [`00bfbec8`](#insn-00bfbec8) → [`00bfbecc`](#insn-00bfbecc)
- ブロック [`00bfbecc`](#insn-00bfbecc) 範囲 `[['00bfbecc', '00bfbed3']]`
  - `CONDITIONAL_JUMP` [`00bfbed0`](#insn-00bfbed0) → [`00bfbee4`](#insn-00bfbee4)
  - `FALL_THROUGH` [`00bfbed0`](#insn-00bfbed0) → [`00bfbed4`](#insn-00bfbed4)
- ブロック [`00bfbed4`](#insn-00bfbed4) 範囲 `[['00bfbed4', '00bfbee3']]`
  - `FALL_THROUGH` [`00bfbee0`](#insn-00bfbee0) → [`00bfbee4`](#insn-00bfbee4)
- ブロック [`00bfbee4`](#insn-00bfbee4) 範囲 `[['00bfbee4', '00bfbef3']]`

## 命令位置別の参照

- [`00bfbea8`](#insn-00bfbea8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbec0`](#insn-00bfbec0) → [`00c5f350`](../00c5f/00c5f350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f350` · 推定シンボル `None` · 推定型 `None`
- [`00bfbec8`](#insn-00bfbec8) → [`00bfbee4`](#insn-00bfbee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbecc`](#insn-00bfbecc) → `Stack[-0x14]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbed0`](#insn-00bfbed0) → [`00bfbee4`](#insn-00bfbee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbee4`](#insn-00bfbee4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbea8`](#insn-00bfbea8)

~~~json
{
  "source": "00bfbea8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbec0`](#insn-00bfbec0)

~~~json
{
  "source": "00bfbec0",
  "target": "00c5f350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbec8`](#insn-00bfbec8)

~~~json
{
  "source": "00bfbec8",
  "target": "00bfbee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbecc`](#insn-00bfbecc)

~~~json
{
  "source": "00bfbecc",
  "target": "Stack[-0x14]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbed0`](#insn-00bfbed0)

~~~json
{
  "source": "00bfbed0",
  "target": "00bfbee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbee4`](#insn-00bfbee4)

~~~json
{
  "source": "00bfbee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
