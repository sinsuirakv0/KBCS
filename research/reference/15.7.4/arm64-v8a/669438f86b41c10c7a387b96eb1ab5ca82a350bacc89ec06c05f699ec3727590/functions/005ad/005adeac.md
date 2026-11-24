# 005adeac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `005adeac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ad/005adeac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0023.md#compare-c85bc462fefeea540abb47c5eb5f8a5d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0032.md#review-1bb2825c802c4b8bf4f206c696386683)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005adeac",
  "name": "FUN_005adeac",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4fb5f1eacf03de2a40b80658e2c4635b43896c66cf649d44ba65506bb0937d2d",
  "source_text_sha256": "4fb5f1eacf03de2a40b80658e2c4635b43896c66cf649d44ba65506bb0937d2d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005adeac",
        "005adee3"
      ]
    ],
    "bytes_sha256": "00fe532a85bfa954cc1446f32a9955904c99468607cb294217ed0e45c2a1c201",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005ab944](../005ab/005ab944.md)
- [005adef8](../005ad/005adef8.md)
- [005ae3c8](../005ae/005ae3c8.md)
- [005ae654](../005ae/005ae654.md)

## 呼び出し先

- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb0c0](../00bdb/00bdb0c0.md)
- [00bdd960](../00bdd/00bdd960.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 354 bytes

~~~c

void FUN_005adeac(void)

{
  undefined8 uVar1;
  
  uVar1 = __cxa_allocate_exception(0x18);
  _ZNSt6__ndk111regex_errorC2ENS_15regex_constants10error_typeE(uVar1,5);
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar1,PTR__ZTINSt6__ndk111regex_errorE_00c1b5b8,
              PTR__ZNSt6__ndk111regex_errorD1Ev_00c1b5c0);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005adeac"></a> `005adeac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-005adeb0"></a> `005adeb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005adeb4"></a> `005adeb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005adeb8"></a> `005adeb8` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-005adebc"></a> `005adebc` | `79 b4 18 94` | bl 0x00bdb0a0 | `UNCONDITIONAL_CALL`
<a id="insn-005adec0"></a> `005adec0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005adec4"></a> `005adec4` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-005adec8"></a> `005adec8` | `a6 be 18 94` | bl 0x00bdd960 | `UNCONDITIONAL_CALL`
<a id="insn-005adecc"></a> `005adecc` | `61 33 00 d0` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-005aded0"></a> `005aded0` | `62 33 00 d0` | adrp x2,0xc1b000 | `FALL_THROUGH`
<a id="insn-005aded4"></a> `005aded4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005aded8"></a> `005aded8` | `21 dc 42 f9` | ldr x1,[x1, #0x5b8] | `FALL_THROUGH`
<a id="insn-005adedc"></a> `005adedc` | `42 e0 42 f9` | ldr x2,[x2, #0x5c0] | `FALL_THROUGH`
<a id="insn-005adee0"></a> `005adee0` | `78 b4 18 94` | bl 0x00bdb0c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005adeac`](#insn-005adeac) 範囲 `[['005adeac', '005adee3']]`

## 命令位置別の参照

- [`005adeac`](#insn-005adeac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005adeb0`](#insn-005adeb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005adebc`](#insn-005adebc) → [`00bdb0a0`](../00bdb/00bdb0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0a0` · 推定シンボル `None` · 推定型 `None`
- [`005adec8`](#insn-005adec8) → [`00bdd960`](../00bdd/00bdd960.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd960` · 推定シンボル `None` · 推定型 `None`
- [`005aded8`](#insn-005aded8) → `00c1b5b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005aded8`](#insn-005aded8) → `00c16810`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTINSt6__ndk111regex_errorE` · 推定型 `pointer __((offset(0x10)))`
- [`005adedc`](#insn-005adedc) → `00c1b5c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005adedc`](#insn-005adedc) → [`00bba418`](../00bba/00bba418.md) · `PARAM` · `ANALYSIS` · 関数 `00bba418` · 推定シンボル `_ZNSt6__ndk111regex_errorD1Ev` · 推定型 `None`
- [`005adee0`](#insn-005adee0) → [`00bdb0c0`](../00bdb/00bdb0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005adeac`](#insn-005adeac)

~~~json
{
  "source": "005adeac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005adeb0`](#insn-005adeb0)

~~~json
{
  "source": "005adeb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005adebc`](#insn-005adebc)

~~~json
{
  "source": "005adebc",
  "target": "00bdb0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005adec8`](#insn-005adec8)

~~~json
{
  "source": "005adec8",
  "target": "00bdd960",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005aded8`](#insn-005aded8)

~~~json
{
  "source": "005aded8",
  "target": "00c1b5b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b5b8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005aded8`](#insn-005aded8)

~~~json
{
  "source": "005aded8",
  "target": "00c16810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16810",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005adedc`](#insn-005adedc)

~~~json
{
  "source": "005adedc",
  "target": "00c1b5c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b5c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005adedc`](#insn-005adedc)

~~~json
{
  "source": "005adedc",
  "target": "00bba418",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005adee0`](#insn-005adee0)

~~~json
{
  "source": "005adee0",
  "target": "00bdb0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
