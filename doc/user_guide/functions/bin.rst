.. _bin:

BIN
===

``BIN`` returns the binary representation of the 64-bit integer value produced from an integer-valued input.

Syntax
------

.. code-block:: sql

   BIN(n)

DESCRIPTION
-----------

================== ================= ====================
Parameter / Return Type              Range
================== ================= ====================
``n``              ``DECIMAL(36,0)`` Integer-valued input
Return             ``VARCHAR(128)``  ``0`` to ``1111111111111111111111111111111111111111111111111111111111111111``
================== ================= ====================

The function returns the binary representation of ``n`` without leading zeros, except that ``0`` is returned as ``0``.

Values above ``18446744073709551615`` saturate to that maximum, values at or below ``-18446744073709551616`` saturate to that maximum, and values in the range ``-18446744073709551615`` to ``-1`` are interpreted as unsigned 64-bit residues.

Given an integer-valued input, the fractional part is ignored.

Negative values are interpreted using a 64-bit two's-complement representation when they fall into the unsigned 64-bit residue range.

``NULL`` input returns ``NULL``.

Examples
--------

.. code-block:: sql

   SELECT BIN(NULL);

Returns ``NULL``.

.. code-block:: sql

   SELECT BIN(0);

Returns ``0`` because no bits are set.

.. code-block:: sql

   SELECT BIN(29);

Returns ``11101``.

.. code-block:: sql

   SELECT BIN(CAST(29 AS DECIMAL(18,0)));

Returns ``11101``.

.. code-block:: sql

   SELECT BIN(CAST(3.14159 AS DECIMAL(18,4)));

Returns ``11``. The input is converted to the function's integer-valued parameter.

.. code-block:: sql

   SELECT BIN(CAST(29.5 AS DOUBLE));

Returns ``11101``.

.. code-block:: sql

   SELECT BIN(CAST(18446744073709551615 AS DECIMAL(36,0)));

Returns ``1111111111111111111111111111111111111111111111111111111111111111``.

.. code-block:: sql

   SELECT BIN(CAST(18446744073709551616 AS DECIMAL(36,0)));

Returns ``1111111111111111111111111111111111111111111111111111111111111111``.

.. code-block:: sql

   SELECT BIN(CAST(-9223372036854775808 AS DECIMAL(36,0)));

Returns ``1000000000000000000000000000000000000000000000000000000000000000``.
