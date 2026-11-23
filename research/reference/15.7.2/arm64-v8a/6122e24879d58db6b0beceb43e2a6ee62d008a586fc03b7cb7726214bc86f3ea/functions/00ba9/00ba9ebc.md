# 00ba9ebc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ba9f84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9f84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0077.md#compare-02af8874af1519fa6303da0890f9bab6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba9ebc",
  "name": "_ZNKSt6__ndk15ctypeIcE10do_tolowerEc",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23d737c9e9593261b65b049c3f5ac8434d537538e84000195356d66f76ba7199",
  "source_text_sha256": "23d737c9e9593261b65b049c3f5ac8434d537538e84000195356d66f76ba7199",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba9ebc",
        "00ba9f47"
      ]
    ],
    "bytes_sha256": "f52d971e445ffc1e06a905b441e0cf0bba2107af99f40e16d5efeec77d36cc65",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)
- [00be1470](../00be1/00be1470.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 444 bytes

~~~c

uint _ZNKSt6__ndk15ctypeIcE10do_tolowerEc(undefined8 param_1,uint param_2)

{
  int iVar1;
  
  if ((param_2 >> 7 & 1) == 0) {
    if (((DAT_010a2898 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_010a2898), iVar1 != 0)) {
      DAT_010a2890 = newlocale(0x1fbf,"C",(__locale_t)0x0);
      __cxa_guard_release(&DAT_010a2898);
    }
    if (0xffffffe5 < (param_2 & 0xff) - 0x5b) {
      param_2 = param_2 + 0x20;
    }
  }
  return param_2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba9ebc"></a> `00ba9ebc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00ba9ec0"></a> `00ba9ec0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ba9ec4"></a> `00ba9ec4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba9ec8"></a> `00ba9ec8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ba9ecc"></a> `00ba9ecc` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00ba9ed0"></a> `00ba9ed0` | `41 01 38 37` | tbnz w1,#0x7,0x00ba9ef8 | `CONDITIONAL_JUMP`
<a id="insn-00ba9ed4"></a> `00ba9ed4` | `c8 27 00 b0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00ba9ed8"></a> `00ba9ed8` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00ba9edc"></a> `00ba9edc` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ba9ee0"></a> `00ba9ee0` | `68 01 00 36` | tbz w8,#0x0,0x00ba9f0c | `CONDITIONAL_JUMP`
<a id="insn-00ba9ee4"></a> `00ba9ee4` | `68 1e 00 12` | and w8,w19,#0xff | `FALL_THROUGH`
<a id="insn-00ba9ee8"></a> `00ba9ee8` | `69 82 00 11` | add w9,w19,#0x20 | `FALL_THROUGH`
<a id="insn-00ba9eec"></a> `00ba9eec` | `08 6d 01 51` | sub w8,w8,#0x5b | `FALL_THROUGH`
<a id="insn-00ba9ef0"></a> `00ba9ef0` | `1f 69 00 31` | cmn w8,#0x1a | `FALL_THROUGH`
<a id="insn-00ba9ef4"></a> `00ba9ef4` | `73 32 89 1a` | csel w19,w19,w9,cc | `FALL_THROUGH`
<a id="insn-00ba9ef8"></a> `00ba9ef8` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00ba9efc"></a> `00ba9efc` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba9f00"></a> `00ba9f00` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ba9f04"></a> `00ba9f04` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00ba9f08"></a> `00ba9f08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ba9f0c"></a> `00ba9f0c` | `c0 27 00 b0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00ba9f10"></a> `00ba9f10` | `00 60 22 91` | add x0,x0,#0x898 | `FALL_THROUGH`
<a id="insn-00ba9f14"></a> `00ba9f14` | `fb c3 00 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00ba9f18"></a> `00ba9f18` | `60 fe ff 34` | cbz w0,0x00ba9ee4 | `CONDITIONAL_JUMP`
<a id="insn-00ba9f1c"></a> `00ba9f1c` | `e1 b7 ff 90` | adrp x1,0x2a5000 | `FALL_THROUGH`
<a id="insn-00ba9f20"></a> `00ba9f20` | `21 28 1a 91` | add x1,x1,#0x68a | `FALL_THROUGH`
<a id="insn-00ba9f24"></a> `00ba9f24` | `e0 f7 83 52` | mov w0,#0x1fbf | `FALL_THROUGH`
<a id="insn-00ba9f28"></a> `00ba9f28` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ba9f2c"></a> `00ba9f2c` | `51 dd 00 94` | bl 0x00be1470 | `UNCONDITIONAL_CALL`
<a id="insn-00ba9f30"></a> `00ba9f30` | `c8 27 00 b0` | adrp x8,0x10a2000 | `FALL_THROUGH`
<a id="insn-00ba9f34"></a> `00ba9f34` | `00 49 04 f9` | str x0,[x8, #0x890] | `FALL_THROUGH`
<a id="insn-00ba9f38"></a> `00ba9f38` | `c0 27 00 b0` | adrp x0,0x10a2000 | `FALL_THROUGH`
<a id="insn-00ba9f3c"></a> `00ba9f3c` | `00 60 22 91` | add x0,x0,#0x898 | `FALL_THROUGH`
<a id="insn-00ba9f40"></a> `00ba9f40` | `f8 c3 00 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00ba9f44"></a> `00ba9f44` | `e8 ff ff 17` | b 0x00ba9ee4 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00ba9ebc`](#insn-00ba9ebc) 範囲 `[['00ba9ebc', '00ba9ed3']]`
  - `CONDITIONAL_JUMP` [`00ba9ed0`](#insn-00ba9ed0) → [`00ba9ef8`](#insn-00ba9ef8)
  - `FALL_THROUGH` [`00ba9ed0`](#insn-00ba9ed0) → [`00ba9ed4`](#insn-00ba9ed4)
- ブロック [`00ba9ed4`](#insn-00ba9ed4) 範囲 `[['00ba9ed4', '00ba9ee3']]`
  - `CONDITIONAL_JUMP` [`00ba9ee0`](#insn-00ba9ee0) → [`00ba9f0c`](#insn-00ba9f0c)
  - `FALL_THROUGH` [`00ba9ee0`](#insn-00ba9ee0) → [`00ba9ee4`](#insn-00ba9ee4)
- ブロック [`00ba9ee4`](#insn-00ba9ee4) 範囲 `[['00ba9ee4', '00ba9ef7']]`
  - `FALL_THROUGH` [`00ba9ef4`](#insn-00ba9ef4) → [`00ba9ef8`](#insn-00ba9ef8)
- ブロック [`00ba9ef8`](#insn-00ba9ef8) 範囲 `[['00ba9ef8', '00ba9f0b']]`
- ブロック [`00ba9f0c`](#insn-00ba9f0c) 範囲 `[['00ba9f0c', '00ba9f1b']]`
  - `CONDITIONAL_JUMP` [`00ba9f18`](#insn-00ba9f18) → [`00ba9ee4`](#insn-00ba9ee4)
  - `FALL_THROUGH` [`00ba9f18`](#insn-00ba9f18) → [`00ba9f1c`](#insn-00ba9f1c)
- ブロック [`00ba9f1c`](#insn-00ba9f1c) 範囲 `[['00ba9f1c', '00ba9f47']]`
  - `UNCONDITIONAL_JUMP` [`00ba9f44`](#insn-00ba9f44) → [`00ba9ee4`](#insn-00ba9ee4)

## 命令位置別の参照

- [`00ba9ec0`](#insn-00ba9ec0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9ec4`](#insn-00ba9ec4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9ed0`](#insn-00ba9ed0) → [`00ba9ef8`](#insn-00ba9ef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9edc`](#insn-00ba9edc) → `010a2898`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ba9ee0`](#insn-00ba9ee0) → [`00ba9f0c`](#insn-00ba9f0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9efc`](#insn-00ba9efc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9f00`](#insn-00ba9f00) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9f10`](#insn-00ba9f10) → `010a2898`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ba9f14`](#insn-00ba9f14) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00ba9f18`](#insn-00ba9f18) → [`00ba9ee4`](#insn-00ba9ee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9f20`](#insn-00ba9f20) → `002a568a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9f2c`](#insn-00ba9f2c) → [`00be1470`](../00be1/00be1470.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1470` · 推定シンボル `None` · 推定型 `None`
- [`00ba9f34`](#insn-00ba9f34) → `010a2890`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ba9f3c`](#insn-00ba9f3c) → `010a2898`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ba9f40`](#insn-00ba9f40) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00ba9f44`](#insn-00ba9f44) → [`00ba9ee4`](#insn-00ba9ee4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba9ec0`](#insn-00ba9ec0)

~~~json
{
  "source": "00ba9ec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9ec4`](#insn-00ba9ec4)

~~~json
{
  "source": "00ba9ec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9ed0`](#insn-00ba9ed0)

~~~json
{
  "source": "00ba9ed0",
  "target": "00ba9ef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9edc`](#insn-00ba9edc)

~~~json
{
  "source": "00ba9edc",
  "target": "010a2898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2898",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba9ee0`](#insn-00ba9ee0)

~~~json
{
  "source": "00ba9ee0",
  "target": "00ba9f0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9efc`](#insn-00ba9efc)

~~~json
{
  "source": "00ba9efc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9f00`](#insn-00ba9f00)

~~~json
{
  "source": "00ba9f00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9f10`](#insn-00ba9f10)

~~~json
{
  "source": "00ba9f10",
  "target": "010a2898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2898",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba9f14`](#insn-00ba9f14)

~~~json
{
  "source": "00ba9f14",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba9f18`](#insn-00ba9f18)

~~~json
{
  "source": "00ba9f18",
  "target": "00ba9ee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9f20`](#insn-00ba9f20)

~~~json
{
  "source": "00ba9f20",
  "target": "002a568a",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9f2c`](#insn-00ba9f2c)

~~~json
{
  "source": "00ba9f2c",
  "target": "00be1470",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba9f34`](#insn-00ba9f34)

~~~json
{
  "source": "00ba9f34",
  "target": "010a2890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2890",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba9f3c`](#insn-00ba9f3c)

~~~json
{
  "source": "00ba9f3c",
  "target": "010a2898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2898",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba9f40`](#insn-00ba9f40)

~~~json
{
  "source": "00ba9f40",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba9f44`](#insn-00ba9f44)

~~~json
{
  "source": "00ba9f44",
  "target": "00ba9ee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
