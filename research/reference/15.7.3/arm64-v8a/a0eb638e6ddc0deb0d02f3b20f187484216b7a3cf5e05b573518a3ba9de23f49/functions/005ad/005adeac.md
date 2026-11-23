# 005adeac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `005adeac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ad/005adeac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0023.md#compare-82eb90c0e13e42660eb62c67d8928cc3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `005adeac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adeac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0023.md#compare-c85bc462fefeea540abb47c5eb5f8a5d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

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
  "source_sha256": "6eae8dc605940ec07f69e9f4ba92ebc150906e0a50edac98ed6fbea5568d9302",
  "source_text_sha256": "6eae8dc605940ec07f69e9f4ba92ebc150906e0a50edac98ed6fbea5568d9302",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005adeac",
        "005adee3"
      ]
    ],
    "bytes_sha256": "00c755d09b446fa23a6b319a96eb086299c528fc97cfb57c195fea82a891ecf0",
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

- [00bdb050](../00bdb/00bdb050.md)
- [00bdb070](../00bdb/00bdb070.md)
- [00bdd910](../00bdd/00bdd910.md)

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
  __cxa_throw(uVar1,PTR__ZTINSt6__ndk111regex_errorE_00c1b568,
              PTR__ZNSt6__ndk111regex_errorD1Ev_00c1b570);
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
<a id="insn-005adebc"></a> `005adebc` | `65 b4 18 94` | bl 0x00bdb050 | `UNCONDITIONAL_CALL`
<a id="insn-005adec0"></a> `005adec0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005adec4"></a> `005adec4` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-005adec8"></a> `005adec8` | `92 be 18 94` | bl 0x00bdd910 | `UNCONDITIONAL_CALL`
<a id="insn-005adecc"></a> `005adecc` | `61 33 00 d0` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-005aded0"></a> `005aded0` | `62 33 00 d0` | adrp x2,0xc1b000 | `FALL_THROUGH`
<a id="insn-005aded4"></a> `005aded4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005aded8"></a> `005aded8` | `21 b4 42 f9` | ldr x1,[x1, #0x568] | `FALL_THROUGH`
<a id="insn-005adedc"></a> `005adedc` | `42 b8 42 f9` | ldr x2,[x2, #0x570] | `FALL_THROUGH`
<a id="insn-005adee0"></a> `005adee0` | `64 b4 18 94` | bl 0x00bdb070 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005adeac`](#insn-005adeac) 範囲 `[['005adeac', '005adee3']]`

## 命令位置別の参照

- [`005adeac`](#insn-005adeac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005adeb0`](#insn-005adeb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005adebc`](#insn-005adebc) → [`00bdb050`](../00bdb/00bdb050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb050` · 推定シンボル `None` · 推定型 `None`
- [`005adec8`](#insn-005adec8) → [`00bdd910`](../00bdd/00bdd910.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd910` · 推定シンボル `None` · 推定型 `None`
- [`005aded8`](#insn-005aded8) → `00c1b568`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005aded8`](#insn-005aded8) → `00c167c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTINSt6__ndk111regex_errorE` · 推定型 `pointer __((offset(0x10)))`
- [`005adedc`](#insn-005adedc) → `00c1b570`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005adedc`](#insn-005adedc) → [`00bba3d4`](../00bba/00bba3d4.md) · `PARAM` · `ANALYSIS` · 関数 `00bba3d4` · 推定シンボル `_ZNSt6__ndk111regex_errorD1Ev` · 推定型 `None`
- [`005adee0`](#insn-005adee0) → [`00bdb070`](../00bdb/00bdb070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb070` · 推定シンボル `None` · 推定型 `None`

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
  "target": "00bdb050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005adec8`](#insn-005adec8)

~~~json
{
  "source": "005adec8",
  "target": "00bdd910",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005aded8`](#insn-005aded8)

~~~json
{
  "source": "005aded8",
  "target": "00c1b568",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b568",
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
  "target": "00c167c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c167c0",
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
  "target": "00c1b570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b570",
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
  "target": "00bba3d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005adee0`](#insn-005adee0)

~~~json
{
  "source": "005adee0",
  "target": "00bdb070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
