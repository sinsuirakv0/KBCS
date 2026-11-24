# 00b7fccc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7fc88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7fc88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0075.md#compare-af15c978bd70742e7e0bd4c3342dbbc0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfc714`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc714.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-234f29fca72b1710198cd75454014e54)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7fccc",
  "name": "FUN_00b7fccc",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d50e3dec66f6fab9042ae056615a8d902b24044d81031fd99d4e22eccd0d922f",
  "source_text_sha256": "d50e3dec66f6fab9042ae056615a8d902b24044d81031fd99d4e22eccd0d922f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7fccc",
        "00b7fd8b"
      ]
    ],
    "bytes_sha256": "1a2c2730259af1f6eb5f83c0ba24f7e63f1c4b1aafc7e2cadf9ae7082e043ef3",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00b7fcc4](../00b7f/00b7fcc4.md)

## 呼び出し先

- [00bdb420](../00bdb/00bdb420.md)
- [00bdb430](../00bdb/00bdb430.md)
- [00bdb440](../00bdb/00bdb440.md)
- [00bdb450](../00bdb/00bdb450.md)
- [00bdcf80](../00bdc/00bdcf80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1002 bytes

~~~c

long * FUN_00b7fccc(long *param_1,undefined8 param_2)

{
  long lVar1;
  long *plVar2;
  undefined1 auStack_30 [8];
  char local_28 [4];
  uint local_24;
  
  local_24 = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC2ERS3_b(local_28,param_1,0);
  if (local_28[0] != '\0') {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_30,(long)param_1 + *(long *)(*param_1 + -0x18));
    plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_30,
                                PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c1bce0
                               );
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    (**(code **)(*plVar2 + 0x38))(plVar2,*(undefined8 *)(lVar1 + 0x28),0,lVar1,&local_24,param_2);
    _ZNSt6__ndk16localeD2Ev(auStack_30);
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | local_24);
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7fccc"></a> `00b7fccc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b7fcd0"></a> `00b7fcd0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b7fcd4"></a> `00b7fcd4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7fcd8"></a> `00b7fcd8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7fcdc"></a> `00b7fcdc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b7fce0"></a> `00b7fce0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b7fce4"></a> `00b7fce4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b7fce8"></a> `00b7fce8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b7fcec"></a> `00b7fcec` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00b7fcf0"></a> `00b7fcf0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00b7fcf4"></a> `00b7fcf4` | `bf c3 1f b8` | stur wzr,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00b7fcf8"></a> `00b7fcf8` | `a2 74 01 94` | bl 0x00bdcf80 | `UNCONDITIONAL_CALL`
<a id="insn-00b7fcfc"></a> `00b7fcfc` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b7fd00"></a> `00b7fd00` | `a8 03 00 34` | cbz w8,0x00b7fd74 | `CONDITIONAL_JUMP`
<a id="insn-00b7fd04"></a> `00b7fd04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b7fd08"></a> `00b7fd08` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00b7fd0c"></a> `00b7fd0c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00b7fd10"></a> `00b7fd10` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00b7fd14"></a> `00b7fd14` | `c3 6d 01 94` | bl 0x00bdb420 | `UNCONDITIONAL_CALL`
<a id="insn-00b7fd18"></a> `00b7fd18` | `e1 04 00 90` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b7fd1c"></a> `00b7fd1c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00b7fd20"></a> `00b7fd20` | `21 70 46 f9` | ldr x1,[x1, #0xce0] | `FALL_THROUGH`
<a id="insn-00b7fd24"></a> `00b7fd24` | `c3 6d 01 94` | bl 0x00bdb430 | `UNCONDITIONAL_CALL`
<a id="insn-00b7fd28"></a> `00b7fd28` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b7fd2c"></a> `00b7fd2c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00b7fd30"></a> `00b7fd30` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00b7fd34"></a> `00b7fd34` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00b7fd38"></a> `00b7fd38` | `28 1d 40 f9` | ldr x8,[x9, #0x38] | `FALL_THROUGH`
<a id="insn-00b7fd3c"></a> `00b7fd3c` | `61 14 40 f9` | ldr x1,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00b7fd40"></a> `00b7fd40` | `a4 13 00 d1` | sub x4,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00b7fd44"></a> `00b7fd44` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b7fd48"></a> `00b7fd48` | `e5 03 14 aa` | mov x5,x20 | `FALL_THROUGH`
<a id="insn-00b7fd4c"></a> `00b7fd4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b7fd50"></a> `00b7fd50` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00b7fd54"></a> `00b7fd54` | `bb 6d 01 94` | bl 0x00bdb440 | `UNCONDITIONAL_CALL`
<a id="insn-00b7fd58"></a> `00b7fd58` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b7fd5c"></a> `00b7fd5c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00b7fd60"></a> `00b7fd60` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00b7fd64"></a> `00b7fd64` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00b7fd68"></a> `00b7fd68` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00b7fd6c"></a> `00b7fd6c` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00b7fd70"></a> `00b7fd70` | `b8 6d 01 94` | bl 0x00bdb450 | `UNCONDITIONAL_CALL`
<a id="insn-00b7fd74"></a> `00b7fd74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7fd78"></a> `00b7fd78` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7fd7c"></a> `00b7fd7c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7fd80"></a> `00b7fd80` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b7fd84"></a> `00b7fd84` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b7fd88"></a> `00b7fd88` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7fccc`](#insn-00b7fccc) 範囲 `[['00b7fccc', '00b7fd03']]`
  - `CONDITIONAL_JUMP` [`00b7fd00`](#insn-00b7fd00) → [`00b7fd74`](#insn-00b7fd74)
  - `FALL_THROUGH` [`00b7fd00`](#insn-00b7fd00) → [`00b7fd04`](#insn-00b7fd04)
- ブロック [`00b7fd04`](#insn-00b7fd04) 範囲 `[['00b7fd04', '00b7fd73']]`
  - `FALL_THROUGH` [`00b7fd70`](#insn-00b7fd70) → [`00b7fd74`](#insn-00b7fd74)
- ブロック [`00b7fd74`](#insn-00b7fd74) 範囲 `[['00b7fd74', '00b7fd8b']]`

## 命令位置別の参照

- [`00b7fcd4`](#insn-00b7fcd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fcd8`](#insn-00b7fcd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fcf4`](#insn-00b7fcf4) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fcf8`](#insn-00b7fcf8) → [`00bdcf80`](../00bdc/00bdcf80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdcf80` · 推定シンボル `None` · 推定型 `None`
- [`00b7fcfc`](#insn-00b7fcfc) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd00`](#insn-00b7fd00) → [`00b7fd74`](#insn-00b7fd74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd14`](#insn-00b7fd14) → [`00bdb420`](../00bdb/00bdb420.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb420` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd20`](#insn-00b7fd20) → `00c1bce0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b7fd20`](#insn-00b7fd20) → `010a2870`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00b7fd24`](#insn-00b7fd24) → [`00bdb430`](../00bdb/00bdb430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb430` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd54`](#insn-00b7fd54) → [`00bdb440`](../00bdb/00bdb440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb440` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd64`](#insn-00b7fd64) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd70`](#insn-00b7fd70) → [`00bdb450`](../00bdb/00bdb450.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb450` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd78`](#insn-00b7fd78) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7fd7c`](#insn-00b7fd7c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7fcd4`](#insn-00b7fcd4)

~~~json
{
  "source": "00b7fcd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fcd8`](#insn-00b7fcd8)

~~~json
{
  "source": "00b7fcd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fcf4`](#insn-00b7fcf4)

~~~json
{
  "source": "00b7fcf4",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fcf8`](#insn-00b7fcf8)

~~~json
{
  "source": "00b7fcf8",
  "target": "00bdcf80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7fcfc`](#insn-00b7fcfc)

~~~json
{
  "source": "00b7fcfc",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fd00`](#insn-00b7fd00)

~~~json
{
  "source": "00b7fd00",
  "target": "00b7fd74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fd14`](#insn-00b7fd14)

~~~json
{
  "source": "00b7fd14",
  "target": "00bdb420",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7fd20`](#insn-00b7fd20)

~~~json
{
  "source": "00b7fd20",
  "target": "00c1bce0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bce0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b7fd20`](#insn-00b7fd20)

~~~json
{
  "source": "00b7fd20",
  "target": "010a2870",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2870",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b7fd24`](#insn-00b7fd24)

~~~json
{
  "source": "00b7fd24",
  "target": "00bdb430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7fd54`](#insn-00b7fd54)

~~~json
{
  "source": "00b7fd54",
  "target": "00bdb440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7fd64`](#insn-00b7fd64)

~~~json
{
  "source": "00b7fd64",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fd70`](#insn-00b7fd70)

~~~json
{
  "source": "00b7fd70",
  "target": "00bdb450",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7fd78`](#insn-00b7fd78)

~~~json
{
  "source": "00b7fd78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7fd7c`](#insn-00b7fd7c)

~~~json
{
  "source": "00b7fd7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
