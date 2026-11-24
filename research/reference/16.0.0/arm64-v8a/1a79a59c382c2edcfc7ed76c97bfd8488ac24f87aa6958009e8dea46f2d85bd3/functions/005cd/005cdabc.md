# 005cdabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0109.md#review-625ad47ee3cde854a98bf7ead5bde8b8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `005cdafc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cdafc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0024.md#compare-4234c4562d07c7c0e35facd15f9ce3eb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cdabc",
  "name": "FUN_005cdabc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc27038fac49334efed3d06d0cc62f5911390438dc1766f3b4faf70c5af65b93",
  "source_text_sha256": "cc27038fac49334efed3d06d0cc62f5911390438dc1766f3b4faf70c5af65b93",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005cdabc",
        "005cdaf3"
      ]
    ],
    "bytes_sha256": "6219483cea30b35d9b9e71d18009e657c7eb86831c78b17ab7dd12cdeb107381",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005cd620](../005cd/005cd620.md)

## 呼び出し先

- [00c57af0](../00c57/00c57af0.md)
- [00c57b10](../00c57/00c57b10.md)
- [00c5a3b0](../00c5a/00c5a3b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 357 bytes

~~~c

void FUN_005cdabc(void)

{
  undefined8 uVar1;
  
  uVar1 = __cxa_allocate_exception(0x18);
  _ZNSt6__ndk111regex_errorC1ENS_15regex_constants10error_typeE(uVar1,0x11);
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar1,PTR__ZTINSt6__ndk111regex_errorE_00c9afb0,
              PTR__ZNSt6__ndk111regex_errorD1Ev_00c9afb8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005cdabc"></a> `005cdabc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-005cdac0"></a> `005cdac0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005cdac4"></a> `005cdac4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005cdac8"></a> `005cdac8` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-005cdacc"></a> `005cdacc` | `09 28 1a 94` | bl 0x00c57af0 | `UNCONDITIONAL_CALL`
<a id="insn-005cdad0"></a> `005cdad0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005cdad4"></a> `005cdad4` | `21 02 80 52` | mov w1,#0x11 | `FALL_THROUGH`
<a id="insn-005cdad8"></a> `005cdad8` | `36 32 1a 94` | bl 0x00c5a3b0 | `UNCONDITIONAL_CALL`
<a id="insn-005cdadc"></a> `005cdadc` | `61 36 00 b0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-005cdae0"></a> `005cdae0` | `62 36 00 b0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-005cdae4"></a> `005cdae4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cdae8"></a> `005cdae8` | `21 d8 47 f9` | ldr x1,[x1, #0xfb0] | `FALL_THROUGH`
<a id="insn-005cdaec"></a> `005cdaec` | `42 dc 47 f9` | ldr x2,[x2, #0xfb8] | `FALL_THROUGH`
<a id="insn-005cdaf0"></a> `005cdaf0` | `08 28 1a 94` | bl 0x00c57b10 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005cdabc`](#insn-005cdabc) 範囲 `[['005cdabc', '005cdaf3']]`

## 命令位置別の参照

- [`005cdabc`](#insn-005cdabc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdac0`](#insn-005cdac0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdacc`](#insn-005cdacc) → [`00c57af0`](../00c57/00c57af0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57af0` · 推定シンボル `None` · 推定型 `None`
- [`005cdad8`](#insn-005cdad8) → [`00c5a3b0`](../00c5a/00c5a3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a3b0` · 推定シンボル `None` · 推定型 `None`
- [`005cdae8`](#insn-005cdae8) → `00c9afb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cdae8`](#insn-005cdae8) → `00c961b8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTINSt6__ndk111regex_errorE` · 推定型 `pointer __((offset(0x10)))`
- [`005cdaec`](#insn-005cdaec) → `00c9afb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cdaec`](#insn-005cdaec) → [`00c36e60`](../00c36/00c36e60.md) · `PARAM` · `ANALYSIS` · 関数 `00c36e60` · 推定シンボル `_ZNSt6__ndk111regex_errorD1Ev` · 推定型 `None`
- [`005cdaf0`](#insn-005cdaf0) → [`00c57b10`](../00c57/00c57b10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b10` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005cdabc`](#insn-005cdabc)

~~~json
{
  "source": "005cdabc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdac0`](#insn-005cdac0)

~~~json
{
  "source": "005cdac0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdacc`](#insn-005cdacc)

~~~json
{
  "source": "005cdacc",
  "target": "00c57af0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdad8`](#insn-005cdad8)

~~~json
{
  "source": "005cdad8",
  "target": "00c5a3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdae8`](#insn-005cdae8)

~~~json
{
  "source": "005cdae8",
  "target": "00c9afb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9afb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdae8`](#insn-005cdae8)

~~~json
{
  "source": "005cdae8",
  "target": "00c961b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c961b8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdaec`](#insn-005cdaec)

~~~json
{
  "source": "005cdaec",
  "target": "00c9afb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9afb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005cdaec`](#insn-005cdaec)

~~~json
{
  "source": "005cdaec",
  "target": "00c36e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdaf0`](#insn-005cdaf0)

~~~json
{
  "source": "005cdaf0",
  "target": "00c57b10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
