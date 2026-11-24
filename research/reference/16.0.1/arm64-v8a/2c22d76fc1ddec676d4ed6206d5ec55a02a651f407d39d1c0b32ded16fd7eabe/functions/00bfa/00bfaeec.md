# 00bfaeec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfaac4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaac4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-a3414344248706c62645da7b9f5fa549)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfaf88`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf88.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-ae4092c106b4cfa3d7a033075c12e1eb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaeec",
  "name": "_ZNSt6__ndk117iostream_categoryEv",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f475e7628c8811590bcd4c0b128ddc9327a9dc40ae279fa30aff00e83a44b70",
  "source_text_sha256": "8f475e7628c8811590bcd4c0b128ddc9327a9dc40ae279fa30aff00e83a44b70",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaeec",
        "00bfaf3b"
      ]
    ],
    "bytes_sha256": "de1217106d0b6e6c336a56da98ea07b99f36150bbb3857b7369f748f906e4409",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 243 bytes

~~~c

undefined ** _ZNSt6__ndk117iostream_categoryEv(void)

{
  int iVar1;
  
  if (((DAT_01127390 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01127390), iVar1 != 0)) {
    __cxa_guard_release(&DAT_01127390);
  }
  return &PTR_PTR_00ca4800;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfaeec"></a> `00bfaeec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfaef0"></a> `00bfaef0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfaef4"></a> `00bfaef4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfaef8"></a> `00bfaef8` | `68 29 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bfaefc"></a> `00bfaefc` | `08 41 0e 91` | add x8,x8,#0x390 | `FALL_THROUGH`
<a id="insn-00bfaf00"></a> `00bfaf00` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bfaf04"></a> `00bfaf04` | `c8 00 00 36` | tbz w8,#0x0,0x00bfaf1c | `CONDITIONAL_JUMP`
<a id="insn-00bfaf08"></a> `00bfaf08` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bfaf0c"></a> `00bfaf0c` | `a0 c7 54 10` | adr x0,0xca4800 | `FALL_THROUGH`
<a id="insn-00bfaf10"></a> `00bfaf10` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bfaf14"></a> `00bfaf14` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfaf18"></a> `00bfaf18` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfaf1c"></a> `00bfaf1c` | `60 29 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00bfaf20"></a> `00bfaf20` | `00 40 0e 91` | add x0,x0,#0x390 | `FALL_THROUGH`
<a id="insn-00bfaf24"></a> `00bfaf24` | `cb 73 01 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00bfaf28"></a> `00bfaf28` | `00 ff ff 34` | cbz w0,0x00bfaf08 | `CONDITIONAL_JUMP`
<a id="insn-00bfaf2c"></a> `00bfaf2c` | `60 29 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00bfaf30"></a> `00bfaf30` | `00 40 0e 91` | add x0,x0,#0x390 | `FALL_THROUGH`
<a id="insn-00bfaf34"></a> `00bfaf34` | `cf 73 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfaf38"></a> `00bfaf38` | `f4 ff ff 17` | b 0x00bfaf08 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfaeec`](#insn-00bfaeec) 範囲 `[['00bfaeec', '00bfaf07']]`
  - `CONDITIONAL_JUMP` [`00bfaf04`](#insn-00bfaf04) → [`00bfaf1c`](#insn-00bfaf1c)
  - `FALL_THROUGH` [`00bfaf04`](#insn-00bfaf04) → [`00bfaf08`](#insn-00bfaf08)
- ブロック [`00bfaf08`](#insn-00bfaf08) 範囲 `[['00bfaf08', '00bfaf1b']]`
- ブロック [`00bfaf1c`](#insn-00bfaf1c) 範囲 `[['00bfaf1c', '00bfaf2b']]`
  - `CONDITIONAL_JUMP` [`00bfaf28`](#insn-00bfaf28) → [`00bfaf08`](#insn-00bfaf08)
  - `FALL_THROUGH` [`00bfaf28`](#insn-00bfaf28) → [`00bfaf2c`](#insn-00bfaf2c)
- ブロック [`00bfaf2c`](#insn-00bfaf2c) 範囲 `[['00bfaf2c', '00bfaf3b']]`
  - `UNCONDITIONAL_JUMP` [`00bfaf38`](#insn-00bfaf38) → [`00bfaf08`](#insn-00bfaf08)

## 命令位置別の参照

- [`00bfaef0`](#insn-00bfaef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf00`](#insn-00bfaf00) → `01127390`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfaf04`](#insn-00bfaf04) → [`00bfaf1c`](#insn-00bfaf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf0c`](#insn-00bfaf0c) → `00ca4800`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfaf10`](#insn-00bfaf10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf20`](#insn-00bfaf20) → `01127390`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfaf24`](#insn-00bfaf24) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf28`](#insn-00bfaf28) → [`00bfaf08`](#insn-00bfaf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf30`](#insn-00bfaf30) → `01127390`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfaf34`](#insn-00bfaf34) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf38`](#insn-00bfaf38) → [`00bfaf08`](#insn-00bfaf08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfaef0`](#insn-00bfaef0)

~~~json
{
  "source": "00bfaef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf00`](#insn-00bfaf00)

~~~json
{
  "source": "00bfaf00",
  "target": "01127390",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127390",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfaf04`](#insn-00bfaf04)

~~~json
{
  "source": "00bfaf04",
  "target": "00bfaf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf0c`](#insn-00bfaf0c)

~~~json
{
  "source": "00bfaf0c",
  "target": "00ca4800",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4800",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfaf10`](#insn-00bfaf10)

~~~json
{
  "source": "00bfaf10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf20`](#insn-00bfaf20)

~~~json
{
  "source": "00bfaf20",
  "target": "01127390",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127390",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfaf24`](#insn-00bfaf24)

~~~json
{
  "source": "00bfaf24",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfaf28`](#insn-00bfaf28)

~~~json
{
  "source": "00bfaf28",
  "target": "00bfaf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf30`](#insn-00bfaf30)

~~~json
{
  "source": "00bfaf30",
  "target": "01127390",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127390",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfaf34`](#insn-00bfaf34)

~~~json
{
  "source": "00bfaf34",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfaf38`](#insn-00bfaf38)

~~~json
{
  "source": "00bfaf38",
  "target": "00bfaf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
