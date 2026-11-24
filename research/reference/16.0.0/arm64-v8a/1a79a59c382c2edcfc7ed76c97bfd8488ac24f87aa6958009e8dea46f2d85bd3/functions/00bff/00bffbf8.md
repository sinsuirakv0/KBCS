# 00bffbf8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b831b0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b831b0.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0020.md#compare-5a4348cf1ecdbf6d034a98240a990b28)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c00020`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00020.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-d1398be33b1d1d89689335cfa9ed85bf)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffbf8",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5uflowEv",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dc78b8a5227dfa2cc60375a0f15abad0d5c263316197fb00d6a8b8aeca18ac44",
  "source_text_sha256": "dc78b8a5227dfa2cc60375a0f15abad0d5c263316197fb00d6a8b8aeca18ac44",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffbf8",
        "00bffc3b"
      ]
    ],
    "bytes_sha256": "433869ed1b622c05cc40d5d2b2b3777e9bd25e94f4e4c0ff818f887978c8639b",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 286 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5uflowEv(long *param_1)

{
  ulong uVar1;
  
  uVar1 = (**(code **)(*param_1 + 0x48))();
  if ((int)uVar1 != -1) {
    uVar1 = (ulong)*(uint *)param_1[3];
    param_1[3] = (long)((uint *)param_1[3] + 1);
  }
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffbf8"></a> `00bffbf8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bffbfc"></a> `00bffbfc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bffc00"></a> `00bffc00` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffc04"></a> `00bffc04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bffc08"></a> `00bffc08` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bffc0c"></a> `00bffc0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bffc10"></a> `00bffc10` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bffc14"></a> `00bffc14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bffc18"></a> `00bffc18` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bffc1c"></a> `00bffc1c` | `80 00 00 54` | b.eq 0x00bffc2c | `CONDITIONAL_JUMP`
<a id="insn-00bffc20"></a> `00bffc20` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bffc24"></a> `00bffc24` | `00 45 40 b8` | ldr w0,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bffc28"></a> `00bffc28` | `68 0e 00 f9` | str x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bffc2c"></a> `00bffc2c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffc30"></a> `00bffc30` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bffc34"></a> `00bffc34` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bffc38"></a> `00bffc38` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffbf8`](#insn-00bffbf8) 範囲 `[['00bffbf8', '00bffc1f']]`
  - `CONDITIONAL_JUMP` [`00bffc1c`](#insn-00bffc1c) → [`00bffc2c`](#insn-00bffc2c)
  - `FALL_THROUGH` [`00bffc1c`](#insn-00bffc1c) → [`00bffc20`](#insn-00bffc20)
- ブロック [`00bffc20`](#insn-00bffc20) 範囲 `[['00bffc20', '00bffc2b']]`
  - `FALL_THROUGH` [`00bffc28`](#insn-00bffc28) → [`00bffc2c`](#insn-00bffc2c)
- ブロック [`00bffc2c`](#insn-00bffc2c) 範囲 `[['00bffc2c', '00bffc3b']]`

## 命令位置別の参照

- [`00bffbfc`](#insn-00bffbfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffc00`](#insn-00bffc00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffc1c`](#insn-00bffc1c) → [`00bffc2c`](#insn-00bffc2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffc2c`](#insn-00bffc2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffc30`](#insn-00bffc30) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffbfc`](#insn-00bffbfc)

~~~json
{
  "source": "00bffbfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffc00`](#insn-00bffc00)

~~~json
{
  "source": "00bffc00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffc1c`](#insn-00bffc1c)

~~~json
{
  "source": "00bffc1c",
  "target": "00bffc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffc2c`](#insn-00bffc2c)

~~~json
{
  "source": "00bffc2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffc30`](#insn-00bffc30)

~~~json
{
  "source": "00bffc30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
