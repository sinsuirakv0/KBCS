# 00ba7ebc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ba7e78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7e78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0077.md#compare-c102ea3805a79702a9fa526fe298761f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c24904`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24904.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0075.md#compare-cdf8ef28c3c37cf800ce3f298c821787)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba7ebc",
  "name": "_ZNSt6__ndk16localeC1Ev",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "75a869019b350a52e6a44e00c6e08cf1576434dde76ac88eee9e1b1d40ebc570",
  "source_text_sha256": "75a869019b350a52e6a44e00c6e08cf1576434dde76ac88eee9e1b1d40ebc570",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba7ebc",
        "00ba7f4b"
      ]
    ],
    "bytes_sha256": "d67a0b4059e0032bac2cee38f33ca46b67a7574da36a9f178a5408e10e71b93a",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdd950](../00bdd/00bdd950.md)

## 呼び出し先

- [00bd6e60](../00bd6/00bd6e60.md)
- [00bdb000](../00bdb/00bdb000.md)
- [00bdb020](../00bdb/00bdb020.md)
- [00bdd980](../00bdd/00bdd980.md)
- [00be18d0](../00be1/00be18d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 617 bytes

~~~c

void _ZNSt6__ndk16localeC1Ev(undefined8 *param_1)

{
  undefined *puVar1;
  bool bVar2;
  int iVar3;
  undefined8 uVar4;
  
  if (((DAT_010a2af0 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_010a2af0), iVar3 != 0)) {
    uVar4 = _ZNSt6__ndk16locale7classicEv();
    _ZNSt6__ndk16localeC1ERKS0_(&DAT_010a2ae8,uVar4);
    __cxa_guard_release(&DAT_010a2af0);
  }
  puVar1 = DAT_010a2ae8;
  bVar2 = DAT_010a2ae8 != &DAT_010a29a0;
                    /* try { // try from 00ba7ef4 to 00ca7eff has its CatchHandler @ 00ba8d5c */
  *param_1 = DAT_010a2ae8;
  if (bVar2) {
    FUN_00bd6e60(1,puVar1 + 8);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba7ebc"></a> `00ba7ebc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00ba7ec0"></a> `00ba7ec0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ba7ec4"></a> `00ba7ec4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba7ec8"></a> `00ba7ec8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ba7ecc"></a> `00ba7ecc` | `c8 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00ba7ed0"></a> `00ba7ed0` | `08 c1 2b 91` | add x8,x8,#0xaf0 | `FALL_THROUGH`
<a id="insn-00ba7ed4"></a> `00ba7ed4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ba7ed8"></a> `00ba7ed8` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ba7edc"></a> `00ba7edc` | `e8 01 00 36` | tbz w8,#0x0,0x00ba7f18 | `CONDITIONAL_JUMP`
<a id="insn-00ba7ee0"></a> `00ba7ee0` | `c8 27 00 f0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00ba7ee4"></a> `00ba7ee4` | `c9 27 00 f0` | adrp x9,0x10a2000 | `FALL_THROUGH`
<a id="insn-00ba7ee8"></a> `00ba7ee8` | `29 81 26 91` | add x9,x9,#0x9a0 | `FALL_THROUGH`
<a id="insn-00ba7eec"></a> `00ba7eec` | `08 75 45 f9` | ldr x8,[x8, #0xae8] | `FALL_THROUGH`
<a id="insn-00ba7ef0"></a> `00ba7ef0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7ef4"></a> `00ba7ef4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00ba7ef8"></a> `00ba7ef8` | `80 00 00 54` | b.eq 0x00ba7f08 | `CONDITIONAL_JUMP`
<a id="insn-00ba7efc"></a> `00ba7efc` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00ba7f00"></a> `00ba7f00` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ba7f04"></a> `00ba7f04` | `d7 bb 00 94` | bl 0x00bd6e60 | `UNCONDITIONAL_CALL`
<a id="insn-00ba7f08"></a> `00ba7f08` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba7f0c"></a> `00ba7f0c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ba7f10"></a> `00ba7f10` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00ba7f14"></a> `00ba7f14` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ba7f18"></a> `00ba7f18` | `c0 27 00 f0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00ba7f1c"></a> `00ba7f1c` | `00 c0 2b 91` | add x0,x0,#0xaf0 | `FALL_THROUGH`
<a id="insn-00ba7f20"></a> `00ba7f20` | `38 cc 00 94` | bl 0x00bdb000 | `UNCONDITIONAL_CALL`
<a id="insn-00ba7f24"></a> `00ba7f24` | `e0 fd ff 34` | cbz w0,0x00ba7ee0 | `CONDITIONAL_JUMP`
<a id="insn-00ba7f28"></a> `00ba7f28` | `6a e6 00 94` | bl 0x00be18d0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba7f2c"></a> `00ba7f2c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ba7f30"></a> `00ba7f30` | `c0 27 00 f0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00ba7f34"></a> `00ba7f34` | `00 a0 2b 91` | add x0,x0,#0xae8 | `FALL_THROUGH`
<a id="insn-00ba7f38"></a> `00ba7f38` | `92 d6 00 94` | bl 0x00bdd980 | `UNCONDITIONAL_CALL`
<a id="insn-00ba7f3c"></a> `00ba7f3c` | `c0 27 00 f0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00ba7f40"></a> `00ba7f40` | `00 c0 2b 91` | add x0,x0,#0xaf0 | `FALL_THROUGH`
<a id="insn-00ba7f44"></a> `00ba7f44` | `37 cc 00 94` | bl 0x00bdb020 | `UNCONDITIONAL_CALL`
<a id="insn-00ba7f48"></a> `00ba7f48` | `e6 ff ff 17` | b 0x00ba7ee0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00ba7ebc`](#insn-00ba7ebc) 範囲 `[['00ba7ebc', '00ba7edf']]`
  - `CONDITIONAL_JUMP` [`00ba7edc`](#insn-00ba7edc) → [`00ba7f18`](#insn-00ba7f18)
  - `FALL_THROUGH` [`00ba7edc`](#insn-00ba7edc) → [`00ba7ee0`](#insn-00ba7ee0)
- ブロック [`00ba7ee0`](#insn-00ba7ee0) 範囲 `[['00ba7ee0', '00ba7ef3']]`
  - `FALL_THROUGH` [`00ba7ef0`](#insn-00ba7ef0) → [`00ba7ef4`](#insn-00ba7ef4)
- ブロック [`00ba7ef4`](#insn-00ba7ef4) 範囲 `[['00ba7ef4', '00ba7efb']]`
  - `CONDITIONAL_JUMP` [`00ba7ef8`](#insn-00ba7ef8) → [`00ba7f08`](#insn-00ba7f08)
  - `FALL_THROUGH` [`00ba7ef8`](#insn-00ba7ef8) → [`00ba7efc`](#insn-00ba7efc)
- ブロック [`00ba7efc`](#insn-00ba7efc) 範囲 `[['00ba7efc', '00ba7f07']]`
  - `FALL_THROUGH` [`00ba7f04`](#insn-00ba7f04) → [`00ba7f08`](#insn-00ba7f08)
- ブロック [`00ba7f08`](#insn-00ba7f08) 範囲 `[['00ba7f08', '00ba7f17']]`
- ブロック [`00ba7f18`](#insn-00ba7f18) 範囲 `[['00ba7f18', '00ba7f27']]`
  - `CONDITIONAL_JUMP` [`00ba7f24`](#insn-00ba7f24) → [`00ba7ee0`](#insn-00ba7ee0)
  - `FALL_THROUGH` [`00ba7f24`](#insn-00ba7f24) → [`00ba7f28`](#insn-00ba7f28)
- ブロック [`00ba7f28`](#insn-00ba7f28) 範囲 `[['00ba7f28', '00ba7f4b']]`
  - `UNCONDITIONAL_JUMP` [`00ba7f48`](#insn-00ba7f48) → [`00ba7ee0`](#insn-00ba7ee0)

## 命令位置別の参照

- [`00ba7ec0`](#insn-00ba7ec0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ec4`](#insn-00ba7ec4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ed8`](#insn-00ba7ed8) → `010a2af0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ba7edc`](#insn-00ba7edc) → [`00ba7f18`](#insn-00ba7f18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7eec`](#insn-00ba7eec) → `010a2ae8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ba7ef8`](#insn-00ba7ef8) → [`00ba7f08`](#insn-00ba7f08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f04`](#insn-00ba7f04) → [`00bd6e60`](../00bd6/00bd6e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e60` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f08`](#insn-00ba7f08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f0c`](#insn-00ba7f0c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f1c`](#insn-00ba7f1c) → `010a2af0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ba7f20`](#insn-00ba7f20) → [`00bdb000`](../00bdb/00bdb000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb000` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f24`](#insn-00ba7f24) → [`00ba7ee0`](#insn-00ba7ee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f28`](#insn-00ba7f28) → [`00be18d0`](../00be1/00be18d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be18d0` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f34`](#insn-00ba7f34) → `010a2ae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ba7f38`](#insn-00ba7f38) → [`00bdd980`](../00bdd/00bdd980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd980` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f40`](#insn-00ba7f40) → `010a2af0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ba7f44`](#insn-00ba7f44) → [`00bdb020`](../00bdb/00bdb020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb020` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f48`](#insn-00ba7f48) → [`00ba7ee0`](#insn-00ba7ee0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba7ec0`](#insn-00ba7ec0)

~~~json
{
  "source": "00ba7ec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ec4`](#insn-00ba7ec4)

~~~json
{
  "source": "00ba7ec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ed8`](#insn-00ba7ed8)

~~~json
{
  "source": "00ba7ed8",
  "target": "010a2af0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2af0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba7edc`](#insn-00ba7edc)

~~~json
{
  "source": "00ba7edc",
  "target": "00ba7f18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7eec`](#insn-00ba7eec)

~~~json
{
  "source": "00ba7eec",
  "target": "010a2ae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba7ef8`](#insn-00ba7ef8)

~~~json
{
  "source": "00ba7ef8",
  "target": "00ba7f08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f04`](#insn-00ba7f04)

~~~json
{
  "source": "00ba7f04",
  "target": "00bd6e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba7f08`](#insn-00ba7f08)

~~~json
{
  "source": "00ba7f08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f0c`](#insn-00ba7f0c)

~~~json
{
  "source": "00ba7f0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f1c`](#insn-00ba7f1c)

~~~json
{
  "source": "00ba7f1c",
  "target": "010a2af0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2af0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba7f20`](#insn-00ba7f20)

~~~json
{
  "source": "00ba7f20",
  "target": "00bdb000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba7f24`](#insn-00ba7f24)

~~~json
{
  "source": "00ba7f24",
  "target": "00ba7ee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f28`](#insn-00ba7f28)

~~~json
{
  "source": "00ba7f28",
  "target": "00be18d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba7f34`](#insn-00ba7f34)

~~~json
{
  "source": "00ba7f34",
  "target": "010a2ae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2ae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba7f38`](#insn-00ba7f38)

~~~json
{
  "source": "00ba7f38",
  "target": "00bdd980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba7f40`](#insn-00ba7f40)

~~~json
{
  "source": "00ba7f40",
  "target": "010a2af0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2af0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba7f44`](#insn-00ba7f44)

~~~json
{
  "source": "00ba7f44",
  "target": "00bdb020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba7f48`](#insn-00ba7f48)

~~~json
{
  "source": "00ba7f48",
  "target": "00ba7ee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
